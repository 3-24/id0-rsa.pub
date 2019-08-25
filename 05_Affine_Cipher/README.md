# [Affine Cipher](https://id0-rsa.pub/problem/5/)

## Brute-Force on a and b

Affine Cipher is better on than Caesar Cipher. However because of the encryption formula ax+b (mod m), a and b each are one of m values(0,1, ... m-1), so there are only m^2^ cases. The given alphabets `ABCDEFGHIJKLMNOPQRSTUVWXYZ ,.` is length m=29. It is not difficult to find normal one in few hundreds cases. If you find one more relation on a and b, the number of cases will decrease more. 

## Frequency Analysis
It is clear that space character `' '` is the most frequent character in the plaintext.  Therefore most frequent character in the ciphertext is the one substituted from space character. From this particular solution, we can get a relation between Affine coefficients a and b, so it helps you to perform brute-forcing.