import hashlib,base64

def get_sha256(s):
    h = hashlib.sha256(s).hexdigest()
    return h

def shash(salt,password):
    hash_val = get_sha256(password + salt)
    return base64.b64encode(hash_val)

def rockyou_bruteforce(salt,output):
    f = open('../rockyou.txt','rb')
    line = f.readline().decode("utf-8")
    while line:
        s = line.strip()
        val = shash(salt,s)
        if (val == output):
            f.close()
            return s
        line = f.readline()
    f.close()
    return None

def main():
    e = open('entry.txt','r')
    eline = e.readline()
    while eline:
        L = eline.strip().split('$')[1:]
        print(rockyou_bruteforce(L[0],L[1]))
        eline = e.readline()
    e.close()
    return

main()
