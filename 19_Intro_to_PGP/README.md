# [Intro_to_PGP](https://id0-rsa.pub/problem/19/)

Very easy problem. Just simply import key and decrypt the ciphertext.

## gpg Importing Key

```console
gpg --import key.txt
```

## gpg Decrypt

``` console
gpg --output decrypted.txt --decrypt encrypted.txt
```


## For More Info
* https://www.gnupg.org/gph/en/manual/x110.html
