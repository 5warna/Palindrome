#Using if else
string = input("Enter the string: ")
if (string == string[:: -1]):
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

