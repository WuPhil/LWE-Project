#An attempt at LWE

#Encryption

#The actual scheme works over a prime on modular arithmetic
#Public parameters: A 1xn (arbitrary) dimensional matrix with random entries (A), a prime modulus (q) 
#Private variables: the bit to send over (M), a secret integer (s), and a matrix of random small errors (e)
#A new matrix B is made with the equation B = s*A + e for each entry in A
#Take the sum of random samples of the values in A (u) and B (v), but add M/2 to B if the bit to encrypt in B is 1
#More public values: the values u and v described above

#Decryption
#Calculate v - su for all of the bits
#If the value is above 1/2, return 1
#Else return 0

#Sidenotes
#We can encrypt an entire message in this program, but it iterates bit by bit
#So one character in the message results in 8 bits, making the results can seem a "bit" large

import numpy as np
import sys
import random
import math

#Important methods

#This is the random sampler that we repeat for each bit
#It also calculates u and v
def get_uv(A,B,bit,q):
	u=0
	v=0
	sample= random.sample(range(nvals-1), nvals//4)
	#If you want to see the random sampling at hand, uncomment the next line:
	#print(sample)
	for x in range(0,len(sample)):
		u=u+(A[sample[x]])
		v= v+B[sample[x]]
	v=v+math.floor(q/2)*bit
	return u%q,v%q

#This is the decryption method
def get_result(u,v,q):
    #If you would like to see more of the decryption, uncomment lines in this method
	res=(v-s*u) % q
	#print(res)
	#print(q)
	if (res>q//2):
		return 1
	return 0

#Convert each character into a string
def tobits(val):
	l = [0]*(8)
	l[0]=val & 0x1
	l[1]=(val & 0x2)>>1
	l[2]=(val & 0x4)>>2
	l[3]=(val & 0x8)>>3
	l[4]=(val & 0x10)>>4
	l[5]=(val & 0x20)>>5
	l[6]=(val & 0x40)>>6
	l[7]=(val & 0x80)>>7
	return l

##Prompting user input
print("All the values entered should be positive integers\n")
q = int(input("How big should the \"ring\" (modulus number) be? This should be prime) "))
s = int(input("What's the secret number? (This should be between 0 and q-1) "))
nvals = int(input("How many elements should the public matrix have? (should be >=16; compiler clutters w/ big values) "))
s = s % q
string = input("What message should be encrypted? ")

A = []
B = []
e = []
M = []

#Creating parameters A,B,e
A = random.sample(range(q), nvals)

for x in range(0,len(A)):
	e.append(random.randint(0,3))
	B.append((A[x]*s+e[x])%q)

#Start converting all of the message to bits
for c in string:
    M.append(tobits(ord(c)))
    
#Outlook on what the method does
print("\n------Parameters and keys-------")
print("Message to cipher:\t",string)
print("Public Key (A):\t",A," and its size is ",len(A))
print("Public Key (B):\t",B)
print("Errors (e):\t\t",e)
print("Secret key:\t\t",s)
print("Prime number:\t\t",q)

print("\n------Sampling Process from public key-------")
#Iterate through all bits, get u and v for each
uentries = []
ventries = []

for byte in M:
    for bit in byte:
        u,v = get_uv(A,B,bit,q)
        uentries.append(u)
        ventries.append(v)

#To hide the big final matrices, comment these lines
print("Entries in u: ", uentries)
print("Entries in v: ", ventries)

print("\n------Results-----------------")
#This is the decryption method
decryptedmatrix = []
for i in range(len(uentries)):
    decryptedmatrix.append(get_result(uentries[i],ventries[i],q))
    
print("Bits at the end: ", decryptedmatrix)

#Finally turning these bits into characters
bytelist = [decryptedmatrix[i:i+8] for i in range(0, len(decryptedmatrix), 8)]
charlist = []

for arr in bytelist:
    a = 0
    for i in range(len(arr)):
        a += (2**i)*arr[i]
    charlist.append(chr(a))

x = ""
for c in charlist:
    x += c
    
print("Resulting message is: ", x)
