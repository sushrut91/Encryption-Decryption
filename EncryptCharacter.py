#!/usr/bin/python3

def main():
    #letters = {'a':0, 'b':1, 'c':2 , 'd':3 , 'e':4, 'f':5 , 'g':6, 'h':7, 'i':8}
    letters = {'a':0, 'b':1, 'c':2 , 'd':3 , 'e':4, 'f':5 , 'g':6, 'h':7, 'i':8, 'j':9, 'k':10 }
    input_char = 'j'
    # b denotes the shift 
    a ,b = 2,len(letters)
    
    if input_char in letters:
        cipher_char = EncryptCharacter(input_char,letters,a,b)
        print(cipher_char)
        plain_char = DecryptCharacter(cipher_char, letters,a,b)
        print(plain_char)
    else:
        print("Please input correct letters")

def DecryptCharacter(encrypt_char, letter_set, a, b):
    #P = a'(x)-b mod p
    #a' = a^(p-2) mod n
    n = len(letter_set)
    plain_char = encrypt_char
    
    if AreRelativePrime(a, n):
        a_inverse = (a ** (n-2)) % n
        plain_char = (a_inverse * (encrypt_char - b)) %n
        
        #Find the key from value 
        for key,value in letter_set.items():
            if value == plain_char:
                return key
    else:
        return "Please change value of a such that a & n are coprime numbers, n is a prime number, n>a"
    
def EncryptCharacter(plain_char, letter_set,a,b):
    # E(x) = (a(x) + b) mod p where a and p should be co-prime
    x = letter_set.get(plain_char)
    n = len(letter_set)
    cipher_char = plain_char
    
    if AreRelativePrime(a,n):
        cipher_char = (a*x + b) % n
        return cipher_char
    else:
        return 'Please change value of a such that a & n are coprime numbers, n is a prime number, n>a'
        
def AreRelativePrime(n1,n2):
# Numbers are relative prime if their GCD is 1, Euclid's algorithm
# Ensure n1 is always greater
# Ensure that n1 is always prime
    flag = False
    
    if n1 > n2:
        flag = isPrime(n1)
    elif n2> n1:
        flag = isPrime(n2)
    else:
        return 'Both a and n cannot be equal for algorithm to work'
        
    if flag:
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
    else:
        return False    
def isPrime(n):
    flag = True
    for i in range(2,n):
        if n % i == 0:
            flag = False
    return flag    
#Run the function main() at startup of the script    
if __name__ == "__main__": main()