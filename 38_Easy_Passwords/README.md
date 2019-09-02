# [38. Easy Passwords](https://rsa-id0.pub/problem/38/)

## /etc/shadow

The password format is the one used in `/etc/shadow`, the collected set of **encrypted** passwords of each user accounts. 
```
$1$abadsalt$0abdVS0D4YnJJ4b7l0RRr1
(1)  (2)             (3)
```
The password information is separated by `$`.

* First field, `1` refers md5 in the encryption algorithm.
* Second field, `abadsalt` refers a salt.
* Third field, `0abdVS0D4YnJJ4b7l0RRr1` refers the encrypted result.


## Brute-Force on Password

We can try just a digits or English words for cracking password. Well, the hint revealed that passwords are English words, so we can try `/usr/share/dict/words`.