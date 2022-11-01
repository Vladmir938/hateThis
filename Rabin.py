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
    p = rnd.randint(1, 1024)
    if prime_num(p) == True and p % 4 == 3:
        return p
    else:
        return generate_key_p()

def generate_key_q(p):
    q = rnd.randint(3, 1024)
    if prime_num(q) == True and math.gcd(p, q) == 1 and q % 4 == 3:
        return q
    else:
        return generate_key_q(p)

def gcd_extended(num1, num2):
    if num1 == 0:
        return (num2, 0, 1)
    else:
        div, x, y = gcd_extended(num2 % num1, num1)
    return (div, y - (num2 // num1) * x, x)

def get_message(path):
    with open(path, encoding='utf-8', mode='r') as file:
        m = hash(file.read())
    return str(m)

def check_message(p, q, n):
    mes1 = get_message(input('Файл_1: '))
    mes2 = get_message(input('Файл_2: '))

    div, yp, yq = gcd_extended(p, q)

    c = hash(mes1) ** 2 % n

    h = hash(mes2) ** 2 % n

    a1 = (yp * p * c + yq * q * h) % n
    a2 = a1 - p

    b1 = (yp * p * c - yq * q * h) % n
    b2 = b1 - q

    return h in [a1, b1, a2, b2]

p = generate_key_p()
q = generate_key_q(p)
n = p * q

print(check_message(p, q ,n))
