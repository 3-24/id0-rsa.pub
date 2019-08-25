# [Intro to Hashing](https://id0-rsa.pub/problem/18/)

## Hashing in Python 3

```python
import hashlib

def md5_string(string):
    return hashlib.md5(string.encode('utf-8')).hexdigest()
```
The hash object in hashlib is feeded by bytes-like-objects. So to hash a string object, it should be encoded in `utf-8`. For more information of `hashlib`, visit https://docs.python.org/3/library/hashlib.html#hash-algorithms.
