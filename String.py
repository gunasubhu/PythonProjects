#Python Program to Check if a String is Palindrome or Not
def IsPalindrome(name):
    if (name==name[::-1]):
        print("This is a polindrome:",name)
    else:
        print("This is not a polindrome:",name)
        
IsPalindrome("Salem")
