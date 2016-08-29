#!/usr/bin/python3

def main():
    letters = {'a':0, 'b':1, 'c':2 , 'd':3 , 'e':4, 'f':5 , 'g':6, 'h':7, 'i':8}
    input_char = 'i'
    
    if input_char in letters:
        cipher_char = EncryptCharacter(input_char,letters)
        print(cipher_char)
    else:
        print("Please input correct letters")

def EncryptCharacter(plain_char, letter_set):
    # E(x) = (a(x) + b) mod p where a and p should be co-prime
    x = letter_set.get(plain_char)
    print(x)
    a = 2
    n = len(letter_set)
    b = 3
    cipher_char = plain_char
    
    if AreRelativePrime(a,n):
        cipher_char = (x + b) % n
        return cipher_char
    else:
        return 'Please change value of a such that a & n are coprime numbers'
        
def AreRelativePrime(n1,n2):
# Numbers are relative prime if their GCD is 1, Euclid's algorithm
# Ensure n1 is always greater
    if n2 > n1 :
        swap = n2
        n2 = n1
        n1 = swap
    remainder = n1
    while n2 > 1:
        remainder = n1 % n2
        n1 = n2
        n2 = remainder
    if remainder == 1:
        return True
    else:
        return False
#Run the function main() at startup of the script    
if __name__ == "__main__": main()