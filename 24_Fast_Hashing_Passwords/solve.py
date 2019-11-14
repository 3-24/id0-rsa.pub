import hashlib

def get_sha256(s):
    print(s)
    h = hashlib.sha256(s).hexdigest()
    return int(h,16)

f = open('rockyou.txt','rb')

sha256_min = 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
sha256_max = 0x0
str_min = None
str_max = None

line = f.readline()
cnt = 1
while line:
    s = line.strip()
    val = get_sha256(s)
    if sha256_min > val:
        sha256_min = val
        str_min = s
    if sha256_max < val:
        sha256_max = val
        str_max = s
    print("Line {}: {}, {}".format(cnt,str_min, str_max))
    line = f.readline()
    cnt+=1

