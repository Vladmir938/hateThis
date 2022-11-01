import random as rnd
import math

def prime_num(num):
    k = 0
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            k = k + 1
    if k <= 0:
        return True
    else:
        return False

def generate_key_p():
    a = rnd.randint(1, 1024)
    if prime_num(a) == True:
        return a
    else:
        return generate_key_p()

def generate_key_q(p):
    q = rnd.randint(3, 1024)
    if (p - 1) % q == 0 and prime_num(q) == True:
        return q
    else:
        return generate_key_q(p)

def generate_a(q, p):
    a = rnd.randint(2, 1024)
    if a ** q % p == 1:
        return a
    else:
        return generate_a(q, p)

def get_message(path):
    with open(path, encoding='utf-8', mode='r') as file:
        m = hash(file.read())
    return str(m)

def check_message(q, a, p):
    s = rnd.randint(2, q - 1)
    v = pow(a, -s, p)

    r = rnd.randint(2, q - 1)

    x1 = pow(a, r, p)

    e1 = hash(get_message(input('Путь к фалу_1: ')) + str(x1))

    y = (r + s * e1) % q

    x2 = (a ** y * v ** (e1 % (p - 1))) % p

    e2 = hash(get_message(input('Путь к фалу_2: ')) + str(x2))

    return e1 == e2

print('Источник: http://kunegin.com/ref8/ecp/schnorr.htm')
p = generate_key_p()
q = generate_key_q(p)
a = generate_a(q, p)

print(check_message(q, a, p))