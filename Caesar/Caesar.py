"""
#Caeser Cipher: one of the simplest and most widely known encryption techniques where Plaintext is encrypted by shifting the letters of the alphabet 3 places forward(left rotation):

   order        0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25
   Plaintext	A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z
   Ciphertext	D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z   A   B   C 
"""

print("Welcome to Caesar Cipher!\n")
    
while True :
    print("========== Menu ==========\n")
    print("1- Encrypt your text\n")
    print("2- Decrypt your ciphertext\n")
    print("3- Exit\n")
        
    c = input("please select an option:\n") 
        
    if c == "1" :
        plaintext = input("please enter your plaintext to encrypt:\n") 
        ciphertext = ""
        plaintext = plaintext.upper()  #convert string to uppercase
        for i in plaintext :
            if i.isalpha() :        
                n = (ord(i) - ord('A') + 3) % 26 + ord('A')  #shifts the letter i by 3 positions in the alphabet:
                """
                ord(i) - ord('A') : convert 'A'-'Z' to 0 - 25
                + 3 : apply the Caesar shift to the left    
                % 26 : wrap-around if past 'Z'(keeps result in 0-25 like X + 3 => 23 + 3 = 26 => 26 % 26 = 0 => A)
                + ord('A') : convert back to ASCII code of the new letter                 
                """
                ciphertext = ciphertext + chr(n)
            else :
                ciphertext = ciphertext + i  #keep space as it is
            
        print("your text is encrypted:" , ciphertext)
        print("\n==============================================\n")
        
    elif c == "2" :
        ciphertext = input("please enter your ciphertext to decrypt:\n") 
        plaintext = ""
        ciphertext = ciphertext.upper()
        for i in ciphertext :
            if i.isalpha() :        
                n = (ord(i) - ord('A') - 3) % 26 + ord('A')  #shifts the letter i by 3 positions in the alphabet:
                """
                ord(i) - ord('A') : convert 'A'-'Z' to 0 - 25
                - 3 : apply the Caesar shift to the right    
                % 26 : wrap-around if it goes before 'A'
                + ord('A') : convert back to ASCII code of the new letter                 
                """
                plaintext = plaintext + chr(n)
            else :
                plaintext = plaintext + i  #keep space as it is
        
        print("your text is decrypted:" , plaintext)
        print("\n==============================================\n")
        
    elif c == "3" :
        print("Thank u for using Caeser :)\nBye!\n")
        print("\n==============================================\n")
        break             
        
    else :
        print("Invalid option! please try again :)\n")


#worst-case time complexity = O(n) where n = length of user input