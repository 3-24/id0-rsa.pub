# [Hello OpenSSL](https://id0-rsa.pub/problem/3/)

## Python OpenSSL RSA Key Implementation

```python
from Crypto.PublicKey import RSA
key = RSA.importKey(open('key.txt').read())
```

Refer to https://pycryptodome.readthedocs.io/en/latest/src/public_key/rsa.html#Crypto.PublicKey.RSA.import_key for more details.


## RSA Decryption

RSA Decryption function for ciphertext c is D(c) = c^d (mod n). Given OpenSSL RSA private key provides all values d and n, so simple modular arithmetic is left.