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

4.#Check if String Contains Substring in Python
def substring(name):
    # substring="Hello Python"
    if "python"in name:
        print("yes!, it is present in the string")
    else:
        print("nope, it is not present in the string")


5.#Python program to accept the strings which contains all vowels
def vowels(name):
    vowel=('a')
    if vowel in name:
        print("This is vowels:',vowel)
    else:
        print("This is not vowels:',vowel)

    
              
vowels('aeiou')

substring("hello python")
    
RemoveWord("Ranjith123")
reverseWord("htijnaR")

IsPalindrome("Salem")
