f = open('ciphertext.txt','r')
ciphertext = f.read()[:-1]
f.close()
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ,.'

p = len(alphabets) # (mod p)

###############################
#### DECRYPT BY OCCURRENCE ####
###############################

alphabets_count = {}
for c in ciphertext:
    if c not in alphabets_count:
        alphabets_count[c] = 1
    else:
        alphabets_count[c] += 1



print(alphabets_count)
c = max(alphabets_count, key = alphabets_count.get)
print('{:s} has maximum occurrence. It would be space.'.format(c))

x = alphabets.index(c)
y = alphabets.index(' ')

print('#{:s}{:d}# decrypted to #{:s}{:d}#'.format(c,x,' ', y))

#############################################
#### BRUTE-FORCE ON a OF LINEAR EQUATION ####
#############################################

# y = ax+b (mod p)

def decrypt(text,a,b):
    plaintext = ''
    for i in range (len(text)):
        c = text[i]
        c_index = alphabets.index(c)
        plaintext += str(alphabets[(a*c_index+b)%p])
    return plaintext

for a in range (1,p):
    b = (y - a*x) % p
    print(a,b,decrypt(ciphertext,a,b)[:20])

# a=21, b=10 looks fine

plaintext = decrypt(ciphertext,21,10)
print(plaintext)

import hashlib

print(hashlib.md5(plaintext.encode('utf-8')).hexdigest())

