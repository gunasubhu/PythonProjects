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

# 4. 
def clearList(mylist):
    print("Mylist data:", mylist)
    mylist *=0
    print("clear the mylist data:", mylist)
    
clearList([1,2,3,4,5])
     
    

    
    
clearList([1,2,3,4,5])  
existsinlist([1,2,3,4,5,6])  
lengthList([1,2,3,4,5,6])      
swaplist([1,2,3,4,5,6])
