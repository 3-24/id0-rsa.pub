import hashlib,crypt

salt = 'abadsalt'

def findPassword(shadow_line):
    f = open('/usr/share/dict/words','r')

    lines = f.readlines()
    for line in lines:
        if "'" in line:
            continue
        word = line.strip()

        if shadow_line == crypt.crypt(word,'$1$abadsalt'):
            return word

    f.close()

def main():
    pwds = open('shadow','r')
    for pwd in pwds:
        pwd = pwd.strip('\n')
        print(findPassword(pwd))

main()
