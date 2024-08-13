#Python Program for array rotation
def rotateArray(arr):
    print(arr[-3:] + arr[0:3])
    

#Python Program for Reversal algorithm for array rotation
def reversedlist(num):
    num2 = []
    for i in num:
        print(i,[i],num2)
        num2 = [i] + num2
    print("reversed list : ", num2)
    
#Python Program to Split the array and add the first part to the end
def splitarr(): 
    mylist=[1,2,3,4,5,6,7]
    firsthalf=mylist[0:4]
    secondhalf=mylist[4:]
    addtwolist=(secondhalf + firsthalf)
    print(addtwolist)

#Python Program for Find reminder of array multiplication divided by n
def findremainder(arr,n):
    mul=1
    for i in arr:
        mul=mul*i
    print(mul)
    print(mul%n)

#Python Program to find sum of array.
def findSumOfArray():
  arr = [1, 2, 3, 4, 5];
  sum = 0;
  for i in range(0, len(arr)):
    sum = sum + arr[i];
  print("Sum of all the elements of an array: " + str(sum));

#Python Program to find largest element in an array
def largestNumber(arr):
    ans=max(arr)
    print(ans)
    

largestNumber([1,4,50,7,10,3])
findremainder([100, 10, 5, 25, 35, 14],11)
reversedlist([1, 2, 3, 4, 5,6,7,8,9]) 
findSumOfArray()  
splitarr()
rotateArray([1,2,3,4,5,6])
