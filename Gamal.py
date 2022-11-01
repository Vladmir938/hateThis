import random as rnd
import math
p = int(input('Введите p: '))
g = int(input('Введите g: '))

x = rnd.randint(p // 2 + 1, p - 3)

with open('eva/text1', encoding='utf-8', mode='r') as file:
    m = hash(file.read())

k = p - 3
while math.gcd(k, p - 1) != 1:
    k = k - 1

y = g ** x % p
r = g ** k % p

s = (pow(k, -1, p - 1) * ((m - x * r) % (p - 1))) % (p - 1)
print(r, s, 'ЭЦП для', m)
res1 = ((y ** r % p) * (r ** s % p) % p)
res2 = g ** (m % (p - 1)) % p
print(res1 == res2)
