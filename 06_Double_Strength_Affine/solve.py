#!/usr/bin/python3

alphstr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ,."
alphdict = {}
for i in range (len(alphstr)):
    alphdict[alphstr[i]] = i

def block_to_num(b):
    assert len(b) == 2
    return 29*alphdict[b[0]] + alphdict[b[1]]

def num_to_block(n):
    return alphstr[n//29] + alphstr[n%29]

f = open("cipher.txt",'r')
ct = f.readline()[:-1]
f.close()

assert len(ct)%2 == 0

'''
for a in range (841):
    for b in range (841):
        pt = ""
        for i in range(len(ct)//2):
            block = ct[2*i] + ct[2*i+1]
            pt += num_to_block( (a*block_to_num(block) + b)%841)
        if " THE" in pt and alphdict[pt[0]] < alphdict[" "] and pt[-1] == ".":
            print(pt,a,b)
'''

# a=714, b=218

pt = "SOME BASIC DEFINITIONS BEFORE WE BEGIN. A BUFFER IS SIMPLY A CONTIGUOUS BLOCK OF COMPUTER MEMORY THAT HOLDS MULTIPLE INSTANCES OF THE SAME DATA TYPE. C PROGRAMMERS NORMALLY ASSOCIATE WITH THE WORD BUFFER ARRAYS. MOST COMMONLY, CHARACTER ARRAYS. ARRAYS, LIKE ALL VARIABLES IN C, CAN BE DECLARED EITHER STATIC OR DYNAMIC. STATIC VARIABLES ARE ALLOCATED AT LOAD TIME ON THE DATA SEGMENT. DYNAMIC VARIABLES ARE ALLOCATED AT RUN TIME ON THE STACK. TO OVERFLOW IS TO FLOW, OR FILL OVER THE TOP, BRIMS, OR BOUNDS. WE WILL CONCERN OURSELVES ONLY WITH THE OVERFLOW OF DYNAMIC BUFFERS, OTHERWISE KNOWN AS STACK BASED BUFFER OVERFLOWS."

import hashlib

print(hashlib.md5(pt.encode()).hexdigest())
