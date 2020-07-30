# LWE-Project

Implementing a very primitive LWE system using Python, and additionally using a public key system over email to encrypt messages.

## Plans/Ideas

-Basic Cryptosystem
* Add more types of encryptions
* Implement some more attacks

-EmaiLWE
* Do some code cleaning (add methods, use the random sample method...)
* Add more types of encryptions

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
* enc(n,q,x,m) -  Encrypts the message bit *m*. *x* will be multiplied with random coefficients and added with error, and *m* * *q*/2 will be added.
* dec(n,q,b,x,a,y) - Decrypts the ciphertext and outputs the message bit *m*. It calculates *z*=*y*-*a* * *x*, and outputs the bit based on the accepted error bound.

### Subroutines:
* check1() - Tests the correctness of a single 0 bit and a single 1 bit. This is run once by default.
* check2(bits) - Tests the correctness of multiple random bits (specified by the number in the input). This is run once by default with 16 bits.
* check3(bits) - Tests correctness of multiple random bits, but only contains one secret key and shows the public information for all the bits encoded as well as the bits encoded.

### Attacks:
* generateBruteForce(n,q,b) - Generates a key that the code attacks by requesting many samples and algorithmically checking every value. By default, a key is considered correct if it properly decrpyts 20 *0* bits and 20 *1* bits.
* sampleBruteForce(n,q,m,b) - Takes *m* * *n* coefficients as the first user input (the first *n* coefficients correspond to the first equation) and *m* outputs to each equation, and finally a third prompt for if there is an expected message. If there is an expected message, then the method solves for the key, otherwise, it will show the most likely key.
* chosenCiphertestAttack(n,q,b) - Generates a secret key and uses the decryption oracle to crack it quickly. Does this by entering ciphertexts with only one coefficient and using the error bounds to find the value of that coefficient in the secret key.

# EmaiLWE
This program was developed to act as an encryption protocol over email using LWE. One person creates a secret and public key (which are secret.txt and pk.txt respectively) and emails only pk.txt to their acquaintance. The other person can use the encrypion method on a bitstring after downloading pk.txt and send over the ciphertext (cipher.txt), which the other person decrypts after downloading.

## Usage
Bob wants to share a message to Alice.
1) Alice uses types "1" with the program to make secret.txt and pk.txt.  
2) Alice shares pk.txt with Bob.  
3) Bob types "2" with the program and enters a bitstring he wants to encrypt, which makes cipher.txt.  
4) Alice types "3" with the program and gets Bob's message

## Contributors

**Gorjan Alagic** - *Mentor*  
**Philip Wu** - *Student*  
**James Zhou** - *Student*
