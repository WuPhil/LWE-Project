# LWE-Project

A very primitive LWE system using Python; possible with many problems.

## Plans/Ideas

* Add more user interaction - allow them to perform chosen-plaintext attacks
* Add subroutines to check the validity of the cryptosystem
* Create methods for encrypting words/images
* Implement more attacks

## Methodology

Parameters: a prime modulus *q*, the number of dimensions *n*, and acceptable error bound *b*.  

LWE is based on multiplying random coefficients over a public key and then adding small errors over modular arithmetic.
This is proven to be at least as hard as worst-case lattice problems on its average case, and is thought to be exponentially hard even for quantum computers to solve.

## Usage

The program is intended to be run in a shell, and will prompt for the parameters.
1) Use the keyGen method to create a key.  
2) Use the enc method on the key and a message bit to encrypt data.  
3) Use the dec method with the key and encrypted data to get the message bit back.

### Methods:
* keyGen(n,q) - generates a secret vector *x* (the "key") which will be used in the other methods.
* enc(n,q,x,m) -  Encrypts the message bit *m*. *x* will be multiplied with random coefficients and added with error, and *m* * *q*/2 will be added .
* dec(n,q,b,x,a,y) - decrypts the ciphertext and outputs the message bit *m*. It calculates *z*=*y*-*a* * *x*, and outputs the bit based on the accepted error bound.

### Subroutines:
* check1() - tests the correctness of a single 0 bit and a single 1 bit. The program runs this once by default.
* check2(bits) - tests the correctness of multiple random bits (specified by the number in the input). This is run once by default with 16 bits.

## Contributors

**Gorjan Alagic** - *Mentor*  
**Philip Wu** - *Student*  
**James Zhou** - *Student*
