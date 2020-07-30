#EmaiLWE: Encrypting messages to use over an email protocol

#Explaining program and prompting choices

import numpy
import random
import math

print("EmaiLWE: A tool to create a public message system with LWE to use over email\n")
print("This program can\n(1) generate keys\n(2) encrypt a bitstring with a public key file\n(3) decrypt from a ciphertext file")
choice = int(input("Choose which option you would like to take: "))

if choice == 1:
    q = int(input("Modulus size: "))
    n = int(input("Number of variables: "))
    m = int(input("Number of equations: "))
    b = q//(2*m)
    
    #Personal/Secret Key creation    
    x = []
    for i in range(n):
        x.append(random.randint(0,q-1))

    #Writing to files
    f = open("secret.txt", "w")
    f.write("q=" + str(q) + "\nn=" + str(n) + "\nm=" + str(m) + "\n")
    f.write(str(x))
    f.close()

    f = open('pk.txt', 'w')
    f.write("q=" + str(q) + "\nn=" + str(n) + "\nm=" + str(m))
    
    #Public Key creation 
    for i in range(m):
        a = []
        for j in range(n):
            a.append(random.randint(0,q-1))
        y = numpy.dot(a,x)
        y == random.randint(0, b)
        y %= q 
        f.write("\n" + str(a))
        f.write("\n" + str(y))

    f.close()

elif choice == 2:
    
    #Reading parameters
    f = open('pk.txt', 'r')
    s = f.readline()
    q = int(s[2:len(s)-1])
    s = f.readline()
    n = int(s[2:len(s)-1])
    s = f.readline()
    m = int(s[2:len(s)-1])
    
    lines = f.read()
    equations = lines.split("\n")
    coefficients = []
    outputs = []

    for i in range(m):
        tempStr = equations[2*i][1:len(equations[2*i])-1]
        tempCoefficient = tempStr.split(", ")
        for j in range(n):
            tempCoefficient[j] = int(tempCoefficient[j])
        coefficients.append(tempCoefficient)
        outputs.append(int(equations[2*i+1]))

    bits = input("What bitstring would you like to encrypt?")

    #there definitely needs to be a lower bound on the number of samples, but not really specified yet
    f = open("cipher.txt", "w")
    for c in bits:
        numSamples = random.randint(m//3,m)
        chosenEquations = []
        for i in range(numSamples):
            chosenEquations.append(random.randint(0,m-1))
        samples = numpy.array([0] * n)
        sampleOutput = 0
        for x in chosenEquations:
            #uncomment any print statement to debug
            #print(x)
            #print(samples)
            #print(coefficients[x])
            samples += numpy.array(coefficients[x])
            sampleOutput += outputs[x]
            

        samples = [s % q for s in samples]
        sampleOutput += (q//2)*int(c) + random.randint(0,q//4)
        sampleOutput %= q
        #print(chosenEquations)
        #print(samples)
        #print(sampleOutput)
        f.write(str(samples) + "\n" + str(sampleOutput) + "\n")
        #print(str(samples) + "\n" + str(sampleOutput))
    f.close()

elif choice == 3:
    #Reading parameters & secret key
    f = open('secret.txt', 'r')
    s = f.readline()
    q = int(s[2:len(s)-1])
    s = f.readline()
    n = int(s[2:len(s)-1])
    s = f.readline()
    m = int(s[2:len(s)-1])
    s = f.readline()
    temp = s[1:len(s)-1]
    x = temp.split(", ")
    x = [int(a) for a in x]
    print(q,n,m,x)

    #Testing the ciphertext equations for decryption
    f = open('cipher.txt', 'r')
    lines = f.read()
    equations = lines.split("\n")
    coefficients = []
    outputs = []

    for i in range(len(equations)//2):
        tempStr = equations[2*i][1:len(equations[2*i])-1]
        tempCoefficient = tempStr.split(", ")
        for j in range(n):
            tempCoefficient[j] = int(tempCoefficient[j])
        coefficients.append(tempCoefficient)
        outputs.append(int(equations[2*i+1]))
    #print(coefficients)
    #print(outputs)

    dec = ""
    for i in range(len(coefficients)):
        z = (outputs[i] - numpy.dot(coefficients[i],x)) % q
        if z<=q//2:
            dec += "0"    
        else:
            dec += "1"

    print("The decrypted message is: ", dec)
    

