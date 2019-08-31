# [2. Hello Bitcoin](https://id0-rsa.pub/problem/2/)

## Elliptic Curve Cryptography

Bitcoin address generation is based on ECC on elliptic curve secp256k1. If you are new to ECC, [Elliptic Curve Cryptography: a gentle introduction](https://andrea.corbellini.name/2015/05/17/elliptic-curve-cryptography-a-gentle-introduction/) would be a great article to join in. Secret key is given number n, and public key H is the point on elliptic curve such that H = nG where G is base point and multiplication is defined on elliptic curve on finite field.
To format the public key, refer [Bitcoin wiki: Elliptic Curve Digital Signature Algorithm](https://en.bitcoin.it/wiki/Elliptic_Curve_Digital_Signature_Algorithm).
## Bitcoin Address

If you generated public key either compressed or uncompressed, the remaining steps are just hashing and encoding. To see full progress, refer [Bitcoin wiki: Technical background of version 1 Bitcoin Address](https://en.bitcoin.it/wiki/Technical_background_of_version_1_Bitcoin_addresses)