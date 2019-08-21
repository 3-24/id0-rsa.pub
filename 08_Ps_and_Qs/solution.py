from Crypto.PublicKey import RSA

c = 0xf5ed9da29d8d260f22657e091f34eb930bc42f26f1e023f863ba13bee39071d1ea988ca62b9ad59d4f234fa7d682e22ce3194bbe5b801df3bd976db06b944da

key1 = RSA.importKey(open('key1.txt').read())
key2 = RSA.importKey(open('key2.txt').read())


// factordb result
p1 = 84131146998723013035726124824393467539823449570683991030677848137795334610229
q1 = 107634389444824136554734231305548679460065919884322199796801660366105198986529

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
