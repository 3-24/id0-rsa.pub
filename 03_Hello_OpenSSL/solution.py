from Crypto.PublicKey import RSA

c = 0x6794893f3c47247262e95fbed846e1a623fc67b1dd96e13c7f9fc3b880642e42

key = RSA.importKey(open('key.txt').read())

print(hex(pow(c,key.d,key.n)))

