# [Hello_PGP](https://id0-rsa.pub/problem/1/)

## Decrypting test_vector

To decrypt the test_vector with password "password", enter
```console
gpg --pinentry-mode loopback --passphrase="password" -d test_vector.txt
```
where test_vector.txt is prepared. Then we can get the original plaintext "hello world".

## Brute-Force on English Words

The proplem is the passphrase is not given. However it is single English word, so we can try brute-force every English word programmatically. Fortunately, linux has built-in English words list in `/usr/share/dict/words`. So simply by skimming this file with above command, we would get the desired result.