import hashlib

def md5_string(string):
    return hashlib.md5(string.encode('utf-8')).hexdigest()


def sha256_string(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()



hash1 = sha256_string('id0-rsa.pub')
hash2 = md5_string(hash1)
print(hash2)
