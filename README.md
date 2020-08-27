# LWE-Project

Implementing a very primitive LWE system using Python, and additionally using a public key system over email to encrypt messages.  

<b>IMPORTANT: This was a student run project, and SHOULD NOT BE USED FOR COMMUNICATING ANY ACTUALLY SENSITIVE INFORMATION. User discretion is advised.</b>

## Table of Contents
-LWE Methodology  
-(LWE Encryption file) Usage  
-Basic Symmetric LWE Methods  
-Symmetric LWE Attacks  
-(Rough) Homomorphic Encryption Implementation  
-EmaiLWE

## Methodology

Parameters: a prime modulus *q*, the number of dimensions *n*, and acceptable error bound *b*.  

LWE is based on multiplying random coefficients over a public key and then adding small errors over modular arithmetic.
This is proven to be at least as hard as worst-case lattice problems on its average case, and is thought to be exponentially hard even for quantum computers to solve.

# LWE_Encryption
## Usage

The program is intended to be run in a shell, and will prompt for the parameters.
1) Use the keyGen method to create a key.  
2) Use the enc method on the key and a message bit to encrypt data.  
3) Use the dec method with the key and encrypted data to get the message bit back.

### Construction Methods:
* keyGen(n,q) - Generates a secret vector *x* (the "key") which will be used in the other methods.
* enc(n,q,x,m) -  Encrypts the message bit *m*. *x* will be multiplied with random coefficients and added with error, and *m***q*/2 will be added.
* dec(n,q,b,x,a,y) - Decrypts the ciphertext and outputs the message bit *m*. It calculates *z*=*y*-*a*·*x*, and outputs the bit based on the accepted error bound.

### Subroutines:
* check1() - Tests the correctness of a single 0 bit and a single 1 bit. This is run once by default.
* check2(bits) - Tests the correctness of multiple random bits (specified by the number in the input). This is run once by default with 16 bits.
* check3(bits) - Tests correctness of multiple random bits, but only contains one secret key and shows the public information for all the bits encoded as well as the bits encoded.

### Oracle Attacks:
* generateBruteForce(n,q,b) - Simulates a possible chosen plaintext attack, which operates by requesting many samples from the encryption method with every possible key given the parameters. Generates a key that the code attacks by requesting many samples and algorithmically checking every value. By default, a key is considered correct if it properly decrpyts 10 *0* bits and 10 *1* bits.
* chosenCiphertestAttack(n,q,b) - Simulates a possible (and effective) chosen ciphertext attack, which operates generally by continuously asking for decryptions of ciphertexts. Generates a secret key and uses the decryption oracle to crack it quickly by entering ciphertexts where the vectors only have a single value with a coefficient of one and using the error bounds to find the value of that coefficient in the secret key.

### Sample Attack
* sampleBruteForce(n,q,m,b) - Takes *m* * *n* coefficients as the first user input (the first *n* coefficients correspond to the first equation) and *m* outputs to each equation, and finally a third prompt for if there is an expected message. If there is an expected message, then the method solves for the key, otherwise, it will show the most likely key.

## FHE Methods
These methods allow LWE encryptions to interact with one another and create encryptions of bits using other encryptions. Currently only the NOT and XOR gate have been developed.
* notct(a,y) - Takes the input of a ciphertext vector and its output and flips its bit (an encryption of *0* becomes *1* and *1* becomes *0*).
* addct(a0,y0,a1,y1) - Adds the 2 vectors (*a0* & *a1*) as well as the inputs (*y0* & *y1*). This can be seen as addition mod 2 with the bits which is equivalent to an XOR gate.  
Checks have been developed for these FHE methods (isnot, isxor, checknot, checkxor).

# EmaiLWE
This program was developed to act as an encryption protocol over email using LWE. It is a public key protocol using LWE and was intended to be used over email, and writes out text files with vectors.

## Usage
Bob wants to share a message to Alice.  
1) Alice uses types "1" with the program to make secret.txt and pk.txt.  
2) Alice shares pk.txt with Bob.  
3) Bob types "2" with the program and enters a bitstring he wants to encrypt, which makes cipher.txt.  
4) Alice types "3" with the program and gets Bob's message.  
In addition, there is AutoEmaiLWE that can be used to check for viable parameters for a secret and public key. To avoid error, some rules to follow are *q* should be less than 10000 and *m* has to be greater than *q*/2 for error to exist.

## Contributors

**Gorjan Alagic** - Mentor <a href="https://www.alagic.org/">[Website]</a>  
**Philip Wu** - Student  
**James Zhou** - Student
