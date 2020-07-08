#LWE Encryption Attempt

import numpy as np
import sys
import random
import math

##Prompting user input
print("All the values entered should be positive integers\n")
q = int(input("Modulus size (q): "))
n = int(input("Number of variables (n): "))
b = int(input("Error bound (b, should be under q/2): "))

#Key generator method
#creates a key for the other methods

def keyGen(n,q):
    x = []
    for i in range(n):
        x.append(random.randint(0,q-1))
    return x

def enc(n,q,x,m):
    a = []
    y = 0
    for i in range(n):
        a.append(random.randint(0,q-1))
    for i in range(n):
        y += a[i] * x[i] + random.randint(0, b//n)
    y += m*q//2 % q
    y %= q
    return a,y

def dec(n,q,b,x,a,y):
    w = 0
    for i in range(n):
        w += a[i] * x[i]
    print(y-w)
    print((y-w)%q, "k")
    z = (y-w) % q
    print(z, "WHAAAAA")
    if z<=b:
        return 0
    else:
        return 1

##Subroutine 1: check if a 0 and 1 bit have correctness
def check1():
    x = keyGen(n,q)

    #Testing a 0 bit
    a0,y0 = enc(n,q,x,0)
    #print("0 bit\na = ", a0,"\ny = ", y0, "\n")
    #Testing a 1 bit
    a1,y1 = enc(n,q,x,1)
    #print("1 bit\na = ", a1,"\ny = ", y1, "\n")
        

    if(dec(n,q,b,x,a0,y0) == 0):
        print("0 successfully decoded")
    else:
        print("0 failed")

    if(dec(n,q,b,x,a1,y1) == 1):
        print("1 successfully decoded")
    else:
        print("1 failed")

print("Performing check 1...")
check1()

##Subroutine 2: Check if random sets of variables & keys properly encrypts some number randomly chosen bits
def check2(bits):
    bitarray = []
    count = 0
    for i in range(bits):
        bitarray.append(random.randint(0,1))
    for i in range(bits):
        x = keyGen(n,q)
        a,y = enc(n,q,x,bitarray[i])
        if(dec(n,q,b,x,a,y) == bitarray[i]):
            count += 1
    print("The currect number of trials was: ", str(count), "/", str(bits))

print("Performing check 2 with 16 bits...")
check2(16)
