from subprocess import run, PIPE

def check(password,filedata):
    print("Trying passphrase={:s}".format(password))
    cmd = run("gpg --pinentry-mode loopback --passphrase '{:s}' -d {:s}".format(password,filedata), shell=True, stdout=PIPE)
    if cmd.returncode == 0:
        output = cmd.stdout.decode('utf-8')
        print('plaintext:')
        print(output)
        return True
    else:
        return False

def main():
    f = open('/usr/share/dict/words','r')
    lines = f.readlines()

    for word in lines:
        if "'" in word:
            continue
        word = word.strip()

        if check(word,'message.txt'):
            break

main()
