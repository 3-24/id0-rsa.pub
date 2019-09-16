#!/usr/bin/python3
import random, fractions

# n = 2^r t
def remove_even(n):
    if n == 0:
        return (0,0)
    r = n
    t = 0
    while (r & 1) == 0:
        t+=1
        r>>=1
    return (r,t)

def get_root_one(x,k,N):
    (r,t) = remove_even(k)
    oldi = None
    i = pow(x,r,N)
    while i != 1:
        oldi = i
        i = (i*i) % N
    if oldi == N-1:
        return None
    return oldi

def factor_rsa(e,d,N):
    k = e*d - 1
    y = None
    while not y:
        x = random.randrange(2,N)
        y = get_root_one(x,k,N)
    p = fractions.gcd(y-1,N)
    q = N // p
    return (p,q)


def get_input():
    f = open('config.txt','r')
    lines = f.readlines()

    N = ''.join(lines[1:19]).replace('\n','').replace(' ','').replace(':','')
    e = 65537
    d = ''.join(lines[21:39]).replace('\n','').replace(' ','').replace(':','')

    N,d = int(N,16), int(d,16)
    return N,e,d

def main():
    N,e,d = get_input()
    p,q = factor_rsa(e,d,N)
    
    if p < q:
        p,q = q,p
    print(q % 100000007)

main()
