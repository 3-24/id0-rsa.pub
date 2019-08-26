# [Ps and Qs](https://id0-rsa.pub/problem/8/)

## Python OpenSSL RSA Key Implementation

```python
from Crypto.PublicKey import RSA
key = RSA.importKey(open('key.txt').read())
```

Refer to https://pycryptodome.readthedocs.io/en/latest/src/public_key/rsa.html#Crypto.PublicKey.RSA.import_key for more details.

## RSA Decryption
Recall that RSA decryption function for ciphertext c is D(c) = c^d (mod n). However, OpenSSL RSA public key doesn't provide d value. Hopefully it has e value, which is used in encryption function for plain test m, E(m) = m^e (mod n). Note that d = e^(-1) mod (phi(n)) where phi is Euler totient function. phi(n) = (p-1)(q-1) where n=pq with two different primes p and q. In conclusion, RSA could be cracked if we can do integer factorization on n!


## FactorDB
* Try http://factordb.com.

## Common Factor Attack
We can try this since two keys are given. Let n1 and n2 be the n of key1 and key2, respectively. If gcd(n1,n2) is not 1, then it is a prime factor of key1!