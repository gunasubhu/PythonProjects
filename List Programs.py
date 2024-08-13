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
    
    
lengthList([1,2,3,4,5,6])      
swaplist([1,2,3,4,5,6])
