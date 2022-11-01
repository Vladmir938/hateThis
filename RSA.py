import random as rnd
import math

p = int(input('Введите p: '))
q = int(input('Введите q: '))

n = p * q

m = (p - 1) * (q - 1)

d = m - 2
while math.gcd(d, m) != 1:
    d = d - 1

e = m - 1
while e != 0:
    e = e - 1
    if e * d % m == 1:
        break

print('Открытый ключ:', e, n, 'Закрытый ключ:', d, n)

with open('eva/text1', encoding='utf-8', mode='r') as file:
    message = hash(file.read())
print('hash =', message)
s1 = message ** (d % (n - 1)) % n
s2 = s1 ** (e % (n - 1)) % n
print(message % n == s2)