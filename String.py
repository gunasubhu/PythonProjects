1. #Python Program to Check if a String is Palindrome or Not
def IsPalindrome(name):
    if (name==name[::-1]):
        print("This is a polindrome:",name)
    else:
        print("This is not a polindrome:",name)

2. #Reverse Words in a Given String in Python
def reverseWord(name):
    rev=name[::-1]
    print("this is reverse string:",rev)


3.#How to Remove Letters From a String in Python
def RemoveWord(name):
    s=name
    print(s.replace("123","kumar"))
    
RemoveWord("Ranjith123")
reverseWord("htijnaR")

IsPalindrome("Salem")
