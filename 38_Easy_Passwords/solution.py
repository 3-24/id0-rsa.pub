import hashlib,crypt

salt = 'abadsalt'

def md5hash(salt,string):
    return crypt.METHOD_MD5(string,salt)
    #return hashlib.md5((salt+string).encode('utf-8')).hexdigest()

def findPassword(shadow_line):
    f = open('/usr/share/dict/words','r')

    lines = f.readlines()
    for line in lines:
        if "'" in line:
            continue
        word = line.strip()

        #print(crypt.crypt(word,'$1$abadsalt'))

        if shadow_line == crypt.crypt(word,'$1$abadsalt'):
            return word

    f.close()

def main():
    pwds = open('shadow','r')
    for pwd in pwds:
        pwd = pwd.strip('\n')
        print(findPassword(pwd))

main()
