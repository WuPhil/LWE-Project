#EmaiLWE: Encrypting messages to use over an email protocol

#Explaining program and prompting choices

import numpy
import random
import math

print("EmaiLWE: A tool to create a public message system with LWE to use over email\n")
print("This program has the option to\n(1) generate keys\n(2) encrypt with a plaintext file\n(3) decrypt from a ciphertext file")
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

    f = open("secret.txt", "w")
        f.write("Mod =" + q + "\nVector size =" + n + "\nEquations =" + q + "\n")

    f.write(str(x))
    f.close()

    f = open('pk.txt', 'w')
    f.write("Mod =" + q + "\nVector size =" + n + "\nEquations =" + q + "\n")
    
    #Public Key creation 
    for i in range(m):
        a = []
        for j in range(n):
            a.append(random.randint(0,q-1))
        y = numpy.dot(a,x)
        y == random.randint(0, b)
        y %= q 
        f.write(str([a,y]) + "\n")


#elif choice == 2:
    #Add file reading for q,n,m
    #randomly sample through all of the equations for every bit to encrypt
    #write out the equations

#elif choice == 3:

