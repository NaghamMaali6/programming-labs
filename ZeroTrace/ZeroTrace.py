""" Count the number of zeros in a given input """

""" *string approach """

print("Welcome to ZeroTrace\n")
print("Please enter a number to count it's zeros :) \n")

number = input()  #take user's input(a string)
counter = 0

if number == '0' :
    counter = 1
    
else :
    counter = number.count('0')  #count how many characters are '0'
        
print(f"The number of zeros in {number} = {counter}")
    
    

#worst-case time complexity = O(n) where n = length of user input

'''
""" *math approach """

print("Welcome to ZeroTrace\n")
print("Please enter a number to count it's zeros :) \n")

number = int(input())  #take integer input
counter = 0

if number == 0 :
    counter = 1
    
else :
    num = abs(number)  #absoloute value to handle negative numbers
    
    while num > 0 :
        d = num % 10  #get last digit
        if d == 0 :
            counter = counter + 1  #when digit is zero
        num = num // 10  #drop last digit
        
print(f"The number of zeros in {number} = {counter}")

#worst-case time complexity = O(n) where n = length of user input

#but this approach doesn't count leading zeros or a numbers with many zeros only (like 00 , 000 , 00000 , ...) so it's discarded 
'''