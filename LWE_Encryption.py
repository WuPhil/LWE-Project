#LWE Encryption Attempt

import numpy
import sys
import random
import math

##Prompting user input
print("All the values entered should be positive integers\n")
q = int(input("Modulus size (q): "))
n = int(input("Number of variables (n): "))
b = int(input("Error bound (b, should be under q/2): "))
print()

def keyGen(n,q):
    x = []
    for i in range(n):
        x.append(random.randint(0,q-1))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    return x

def enc(n,q,x,m):
    a = []
    for i in range(n):
        a.append(random.randint(0,q-1))
    y = numpy.dot(a,x)
    error = random.randint(0, b)
    y += m*q//2 + error
    y %= q 
    return a,y

def dec(n,q,b,x,a,y):
    z = (y - numpy.dot(a,x)) % q
    if z<=b:
        return 0
    else:
        return 1

##Subroutine 1: check if a 0 and 1 bit have correctness
def check1():
    x = keyGen(n,q)
    print("Secret key:", x)
    
    print("Testing correctness of a 0 bit")
    a0,y0 = enc(n,q,x,0)
    print("a = ", a0,"\ny = ", y0, "\n")

    
    print("Testing correctness of a 1 bit")
    a1,y1 = enc(n,q,x,1)
    print("a = ", a1,"\ny = ", y1, "\n")
        
    
    if(dec(n,q,b,x,a0,y0) == 0):
        print("0 bit successfully decoded")
    else:
        print("0 bit failed")

    if(dec(n,q,b,x,a1,y1) == 1):
        print("1 bit successfully decoded")
    else:
        print("1 bit failed")

print("Checking correctness of one 0 and 1\n")
check1()

##Subroutine 2: Check if random bits are correct with the key
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

print("\nChecking correctness of 16 random bits...")
check2(16)

##Brute Force Attack: generates a key and checks every key value until a valid key (passes c many "0" and "1" bits) is found
# Don't try with n or q above 10
def bruteForce(q, n):
    x = keyGen(n,q)
    print("The actual key is", x)
    test = [0] * n
    highest = 0
    for i in range(q**n):
        count = 0
        likelyKey = []
        for j in range(20):
            #0 bit test
            a,y = enc(n,q,x,0)
            if (y - numpy.dot(a,test)) % q <= b:
                count += 1

            #1 bit test
            a,y = enc(n,q,x,1)
            if (y - numpy.dot(a,test)) % q > b:
                count += 1
        
        if count > highest:
            highest = count
            likelyKey = test

        ##shows the most likely key
        if count == 40:
            print("A highly likely value for the key is", test)
            return test
        else:
            test[0] += 1
            for j in range(n-1):
                #Uncomment the following line to track how the code is operating, but it slows calculation
                print(count, "many correct evaluations for", test)
                if test[j] == q:
                    test[j] = 0
                    test[j+1] += 1
                if test[n-1] == q:
                    print("None of the keys fully worked, but the best one was", likelyKey, "with a", highest/40, "success rate")
