from Crypto.PublicKey import RSA
import math

c = 0xf5ed9da29d8d260f22657e091f34eb930bc42f26f1e023f863ba13bee39071d1ea988ca62b9ad59d4f234fa7d682e22ce3194bbe5b801df3bd976db06b944da

key1 = RSA.importKey(open('key1.txt').read())
key2 = RSA.importKey(open('key2.txt').read())

g = math.gcd(key1.n, key2.n)

print('g:',g)

p1 = g
q1 = key1.n//g

assert p1*q1 == key1.n


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

d = modinv(key1.e,(p1-1)*(q1-1))

print(hex(pow(c,d,key1.n)))
