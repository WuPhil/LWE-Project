#EmaiLWE: Encrypting messages to use over an email protocol

#Explaining program and prompting choices

import numpy
import random
import math

print("EmaiLWE: A tool to create a public message system with LWE to use over email\n")
print("This program can\n(1) generate keys\n(2) encrypt a bitstring with a public key file\n(3) decrypt from a ciphertext file")
print("In development is (4) the homomorphic encryption and (5) decryption scheme")
#choice = int(input("Choose which option you would like to take: "))

def readInt(f):
    s = f.readline()
    return int(s[2:-1])


#q = int(input("Modulus size: "))
#n = int(input("Number of variables: "))
q = 100
n = 4
ring = "y"

x = numpy.random.randint(0, q-1, size = n)

f = open("secret.txt", "w")
f.write("q=" + str(q) + "\nn=" + str(n) + "\n" + str(list(x)))
f.close()

f = open('pk.txt', 'w')
f.write("q=" + str(q) + "\nn=" + str(n) + "\n")

if ring == "y":
    b = q//(2*n)
    f.write("m=" + str(n) + "\nRLWE\n")
    a = numpy.random.randint(0, q-1, size = n)
    f.write(str(list(a)) + "\n")
    for i in range(n):
        f.write(str((numpy.dot(a,x) + random.randint(0, b)) % q) + "\n")
        a = numpy.append(a[1:], a[0])
 
else:
    #m = int(input("Number of Equations: "))
    m = 6
    f.write("m=" + str(m))
    b = q//(2*m)
    for i in range(m):
        a = numpy.random.randint(0, q-1, size = n)
        y = numpy.dot(a,x) + random.randint(0, b)
        y %= q
        f.write("\n" + str(list(a)))
        f.write("\n" + str(y))

f.close()

f = open('pk.txt', 'r')
q = readInt(f)
n = readInt(f)
m = readInt(f)
coefficients = []
outputs = []
s = f.readline()

if s == "RLWE\n":
    tempStr = f.readline()
    tempCoefficient = tempStr[1:-2].split(", ")
    publicVector = [int(s) for s in tempCoefficient]
    coefficients.append(publicVector)
    lines = f.read()
    equations = lines.split("\n")
    for i in range(n):
        publicVector.append(publicVector.pop(0))
        coefficients.append(publicVector.copy())
        outputs.append(int(equations[i]))
 
else:
    lines = s + f.read()
    equations = lines.split("\n")
    for i in range(m):
        tempStr = equations[2*i][1:-1]
        tempCoefficient = tempStr.split(", ")
        tempCoefficient = [int(s) for s in tempCoefficient]
        coefficients.append(tempCoefficient)
        outputs.append(int(equations[2*i+1]))
#print(coefficients)
#print(outputs)

bits = "10101010101010101010101010101010101010"

#there definitely needs to be a lower bound on the number of samples, but not really specified yet
f = open("cipher.txt", "w")
for c in bits:
    numSamples = random.randint(m//3,m)
    chosenEquations = numpy.random.randint(0, m-1, size = numSamples)
    samples = [0] * n
    sampleOutput = 0
    #print(chosenEquations)
    for x in chosenEquations:
        samples = numpy.add(samples,coefficients[x])
        sampleOutput += outputs[x]
     
    samples = [s % q for s in samples]
    sampleOutput += (q//2)*int(c)
    sampleOutput %= q
    f.write(str(samples) + "\n" + str(sampleOutput) + "\n")
    
f.close()

#Reading parameters & secret key
f = open('secret.txt', 'r')
q = readInt(f)
n = readInt(f)

temp = f.readline()[1:-1]
x = temp.split(", ")
x = [int(a) for a in x]

#Testing the ciphertext equations for decryption
f = open('cipher.txt', 'r')
lines = f.read()
equations = lines.split("\n")
coefficients = []
outputs = []

for i in range(len(equations)//2):
    tempStr = equations[2*i][1:-1]
    tempCoefficient = tempStr.split(", ")
    for j in range(n):
        tempCoefficient[j] = int(tempCoefficient[j])
    coefficients.append(tempCoefficient)
    outputs.append(int(equations[2*i+1]))

dec = ""
for i in range(len(coefficients)):
    z = (outputs[i] - numpy.dot(coefficients[i],x)) % q
    if z<=q//2:
        dec += "0"    
    else:
        dec += "1"

print("The decrypted message is: ", dec)
    
#elif choice == 4:
    



