#Python program to interchange first and last elements in a list.
#Python program to swap two elements in a list
def swaplist(arr):
     arr1=arr[-1:]
     arr3=arr[1:5]
     arr2=arr[0:1]
     print("Original possition in list:",arr[0:6])
     print("Swap the possition in list values:",  arr1 + arr3 + arr2)

#Python | Ways to find length of list
def lengthList(arr):
    length=len(arr)
    print("Length of list:",length)

#Python | Ways to check if element exists in list.
def existsinlist(lst):
    val=10
    if val in lst:
        print(f"{val} is available in the list.")
    else:
        print(f"{val} is not available in tha list.")
    
    
#Different ways to clear a list in Python
# 1. clear()
def clearList(mylist):
    print("Mylist data:", mylist)
    mylist.clear()
    print("clear the mylist data:", mylist)

# 2. delete the particlar index
def clearList(mylist):
    print("Mylist data:", mylist)
    del mylist[2]
    print("clear the mylist data:", mylist)

# 3. delete the list
def clearList(mylist):
    print("Mylist data:", mylist)
    del mylist[:]
    print("clear the mylist data:", mylist)

# 4. Using *=0
def clearList(mylist):
    print("Mylist data:", mylist)
    mylist *=0
    print("clear the mylist data:", mylist)
    
# 5.List Re-Initialization
def clearList(mylist):
    print("Mylist data:", mylist)
    mylist = []
    print("clear the mylist data:", mylist)


# 1. Python program to find sum of elements in list
def sumofList(mylist):
    sumoflist=sum(mylist)
    print("Sum of the list:", sumoflist)


# 2.
def sumofList(mylist):
    total = 0
    for i in mylist:
        total = total + i
    print(f"Sum of the element list is : {total}")


# Python | Multiply all numbers in the list
def multiplyofList(mylist):
    total = 1
    for i in mylist:
        total = total * i
    print(f"Sum of the element list is : {total}")


# 1. Reversing a List in Python(Slicing technique)
def reverseList(mylist):
    list1=mylist[::-1]
    print(f"Reverse the list : {list1}")
     
# 2. Reversing a List in Python(Reverse method)
def reverseList(mylist):
    list1=list(reversed(mylist))
    print(f"Reverse the list : {list1}")

#Python program to find smallest number in a list
def MinimumNumberOfList(mylist):
    list1=min(mylist)
    print(f"Minimum number of list : {list1}")


#Python program to find largest number in a list
def MaximumNumberOfList(mylist):
    list1=min(mylist)
    print(f"Maximum number of list : {list1}")

#Python program to find second largest number in a list
def secondlargenumberlist(mylist):
    mylist.sort()
    print(mylist[-2])


#Python program to find second smallest number in a list
def secondsmallestnumberlist(mylist):
    mylist.sort()
    print(mylist[2])

#Python program to find N largest elements from a list
def nlargenumberlist(mylist):
    n=4
    mylist.sort()
    print(mylist[-n:])


#Python program to print even numbers in a list
def evenlist(num):
    print("even numbers:")
    for i in num:
        if i % 2 == 0:
            print(i,end=" ")


#Python program to print odd numbers in a list
def OddNumberList(num):
    print("Odd numbers:")
    for i in num:
        if i % 2 != 0:
            print(i,end=" ")

#Python program to print all even numbers in a range
def AllEvenNumber(num1,num2):
    print("All even  numbers:")
    for i in range(num1,num2):
        if i % 2 == 0:
            print(i,end=" ")

#Python program to print all even numbers in a range
def AllOddNumber(num1,num2):
    print("All even  numbers:")
    for i in range(num1,num2):
        if i % 2 != 0:
            print(i,end=" ")

#Python program to print positive numbers in a list
def positiveNumberslist(num):
    print("Positive numbers in a list")
    for i in num:
        if i >=0:
            print(i, end=' ')


#Python program to print negative numbers in a list
def NagativeNumberslist(num):
    print("Nagative numbers in a list")
    for i in num:
        if i < 0:
            print(i, end=' ')

#Python program to print all positive numbers in a range
def AllPositiveNumberslist(num1,num2):
    print("Positive numbers in a list")
    for i in range(num1,num2):
        if i >=0:
            print(i, end=' ')

#Python program to print all nagative numbers in a range
def AllNagativeNumberslist(num1,num2):
    print("Nagative numbers in a list")
    for i in range(num1,num2):
        if i < 0:
            print(i, end=' ')

#Remove multiple elements from a list in Python
def Remove_Multiple_Elements_List(num):
    print("Remove multiple numbers in a list")
    for i in num:
        del num[1:5]
        print(i, end=' ')

# Python Code to Remove empty List from List
def empty_list_remove(mylist):
    print("removed empty list")
    emptylist = []
    for i in mylist:
        if i != emptylist:
            print(i, end=' ')


empty_list_remove([5, 6, [], 3, [], [], 9])         

Remove_Multiple_Elements_List([11, 5, 17, 18, 23, 50,22])       

AllNagativeNumberslist(-4,8)
AllPasitiveNumberslist(-4,8)  
NagativeNumberslist([10,2,-4,7,-9])         
positiveNumberslist([10,2,-4,7,-9])       
AllOddNumber(8,30)       
AllEvenNumber(8,30)       
OddNumberList([5,1,7,9,10,2,6,])
evenlist([5,1,7,9,10,2,6,])     
nlargenumberlist([10,50,20,40,15,23])
secondsmallestnumberlist([1,2,6,4,5,3])
secondlargenumberlist([1,2,6,4,5,3])
MaximumNumberOfList([1,2,3,4,5])
MinimumNumberOfList([1,2,3,4,5])
reverseList([1,2,3,4,5]) 
multiplyofList([1,2,3])
sumofList([10,20,1,3])      
clearList([1,2,3,4,5])  
existsinlist([1,2,3,4,5,6])  
lengthList([1,2,3,4,5,6])      
swaplist([1,2,3,4,5,6])
