#LWE Encryption System

import numpy
import random
import math

##Prompting user input
print("All the values entered should be positive integers\n")
q = int(input("Modulus size (q): "))
n = int(input("Number of variables (n): "))
b = int(input("Error bound (b, should be under q/4): "))
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

##Subroutine 2: Check if random bits are correct with various different key
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

##Subroutine 3: Check if random bits are correctly decrypted with a single key - prints out the key, message, and samples
#Used for debugging
def check3(bits):
    bitarray = []
    count = 0
    x = keyGen(n,q)
    print(x)
    for i in range(bits):
        bitarray.append(random.randint(0,1))
    print(bitarray)
    for i in range(bits):
        a,y = enc(n,q,x,bitarray[i])
        print("Coefficient vector:", a)
        print("Output:", y)
        if(dec(n,q,b,x,a,y) == bitarray[i]):
            count += 1
    print("The currect number of trials was: ", str(count), "/", str(bits))

##Generated Brute Force Attack: generates a key and checks every key value until a valid key (passes c many "0" and "1" bits) is found
# Don't try with n or q above 10
def generateBruteForce(n,q,b):
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
                #print(count, "many correct evaluations for", test)
                if test[j] == q:
                    test[j] = 0
                    test[j+1] += 1
                if test[n-1] == q:
                    print("None of the keys fully worked, but the best one was", likelyKey, "with a", highest/40, "success rate")
                    
##Sample LWE Attack: takes m LWE samples with error bound b and finds the most likely message by trying all possible keys
#Alternatively, if there is an expected message (bitstring) than the program will output the most likely keys
def sampleBruteForce(n,q,m,b):
    coeffs = []
    outputs = []
    test = [0] * n
    print("Enter the", n*m, "coefficients from the samples with space separation:")
    coeffstring = str(input()).split()
    for j in range(n*m):
        coeffstring[j] = int(coeffstring[j])
    coeffs = [coeffstring[i * n:(i + 1) * n] for i in range((len(coeffstring) + n - 1) // n )]  
    print("Enter the output for every equation here")
    outputs = str(input()).split()
    for j in range(m):
        outputs[j] = int(outputs[j])
    message = str(input("Enter expected message here (must be length m) or leave blank to find most likely message): "))

    if len(message) == 0:
        possibleMessages = []
        scores = []
        for i in range(q**n):
            currentMessage = ""
            for j in range(m):
                  if (outputs[j] - numpy.dot(test,coeffs[j])) % q <= b:
                      currentMessage += "0"
                  else:
                      currentMessage += "1"
            if currentMessage in possibleMessages:
                  ind = possibleMessages.index(currentMessage)
                  scores[ind] += 1
            else:
                  possibleMessages.append(currentMessage)
                  scores.append(1)
            test[0] += 1
            for j in range(n-1):
                if test[j] == q:
                    test[j] = 0
                    test[j+1] += 1
        #Uncomment following line to see every possible message that the string could've been
        #print(possibleMessages)
        highest = max(scores)
        #Uncomment following line to see the number of times the message corresponding to the position in the possibleMessages was decrypted
        #print("Scores", scores)
        positions = [i for i, j in enumerate(scores) if j == highest]
        likelyMessages = []
        for i in positions:
            likelyMessages.append(possibleMessages[i])
        print("The most likely message(s) were", likelyMessages, "with a", highest/(q**n), "probability")

    elif len(message) == m:
        possibleKeys = []
        for i in range(q**n):
            currentMessage = ""
            for j in range(m):
                  if (outputs[j] - numpy.dot(test,coeffs[j])) % q <= b:
                      currentMessage += "0"
                  else:
                      currentMessage += "1"
            if currentMessage == message:
                possibleKeys.append(test.copy())
            test[0] += 1
            for j in range(n-1):
                if test[j] == q:
                    test[j] = 0
                    test[j+1] += 1
            #Uncomment following line to see which vector decrypted to what message
            #print("Current vector testing", test)
        print("Some possible keys were", possibleKeys)

#A new situation is having the attacker be given access to decryption and encryption
#The attacker may decrypt any message, as long as it is not 
#It should be noted that my version of LWE is not resistant to this attack

def chosenCiphertextAttack(n,q,b):
    x = keyGen(n,q)
    print("Secret key is", x)
    test = [0] * n
    final = []
    test[0] = 1
    for i in range(n):
        testBit = dec(n,q,b,x,test,0)
        if testBit == 1:
            y = 0
            while dec(n,q,b,x,test,y) == 1:
                y += 1
            final.append(y)
        else:
            y = q
            while dec(n,q,b,x,test,y) == 0:
                y -= 1
            final.append(y+1)
        current = test.index(1)
        test[current] = 0
        if i < n-1:
            test[current+1] = 1
    print("The discovered key was", final)

def addct(a0,y0,a1,y1):
    a = []
    for i in range(len(a0)):
        a.append((a0[i] + a1[i]) % q)
    y = (y0 + y1) % q
    return a,y

def notct(a,y):
    return a, (y+q//2)%q

def isnot(x,a,y):
    a,y = notct(a,y)
    z = (y - numpy.dot(a,x)) % q
    if z<=b:
        return 0
    else:
        return 1

def isxor(x,a0,y0,a1,y1):
    a,y = addct(a0,y0,a1,y1)
    z = (y - numpy.dot(a,x)) % q
    if z<q//2:
        return 0
    else:
        return 1

def checknot(bits):
    count = 0
    for i in range(bits):
        x = keyGen(n,q)
        a,y = enc(n,q,x,0)
        if isnot(x,a,y) == 1:
            count += 1
        else:
            print("not 0 failed")
        a,y = enc(n,q,x,1)
        if isnot(x,a,y) == 0:
            count += 1
        else:
            print("not 1 failed")
    print("There were a total of", count, "/", 2*bits, "working nots")

def checkxor(bits):
    count = 0
    for i in range(bits):
        x = keyGen(n,q)
        a0,y0 = enc(n,q,x,0)
        a1,y1 = enc(n,q,x,1)
        
        if isxor(x,a0,y0,a1,y1) == 1:
            #print("xor 0 1 worked")
            count += 1
        else:
            print("xor 0 1 failed")
            
        if isxor(x,a1,y1,a0,y0) == 1:
            #print("xor 1 0 worked")
            count += 1
        else:
            print("xor 1 0 failed")
            
        if isxor(x,a0,y0,a0,y0) == 0:
            #print("xor 0 0 worked")
            count += 1
        else:
            print("FAILED xor 0 0")
            
        if isxor(x,a1,y1,a1,y1) == 0:
            #print("xor 1 1 worked")
            count += 1
        else:
            print("FAILED 1 1")
    print("There were a total of", count, "/", 4*bits, "working xors")
        
