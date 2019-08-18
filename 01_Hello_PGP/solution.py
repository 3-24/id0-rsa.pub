import subprocess

f = open('/usr/share/dict/words','r')

lines = f.readlines()

for line in lines:
    if "'" in line:
        continue
    line = line.strip()
    try:
        result = subprocess.check_output("gpg --passphrase='{:s}' -d message.txt".format(line), shell=True)
    except subprocess.CalledProcessError:
        print(line)
        continue
    print('Cracked!! The keyword is {:s}, decrypted message is:'.format(line))
    print(result)
    break
