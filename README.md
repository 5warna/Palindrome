#Palindrome of String

#Using if else

string = input("Enter the string: ")

if (string == string[::1]:

    print("The string is a Palindrome")

else:
    
    print("The string is not a Palindrome")

#Using def function

def isPalindrome(s):
    
    return s == s[:: -1]

string = input("Enter the string: ")

reverse = isPalindrome(string)

if reverse:
    
    print(string, "is a Palindrome")

else:
    
    print(string, "is not a Palindrome")

    
#Palindrome of Number

#Using while loop with if else

n = int(input("Enter number: "))

num = n

rev = 0

while (n > 0):
    
    rev = rev * 10 + n % 10
    
    n = n // 10

if (num == rev):
    
    print("The number is a Palindrome")

else:
    
    print("The number is not a Palindrome")

#Using def function

def isPalindrome(n):
    
    rev = 0
    
    while (n != 0):
        
        rev = rev * 10 + n % 10
        
        n = n // 10
    
    return rev

num = int(input("Enter the number: "))

rev = isPalindrome(num)

if (num == rev):
    
    print(num, "is a Palindrome")

else:
    
    print(num, "is not a Palindrome")
