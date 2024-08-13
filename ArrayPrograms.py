
#Reverse the list
def reversedlist(num):
    num2 = []
    for i in num:
        print(i,[i],num2)
        num2 = [i] + num2
    print("reversed list : ", num2)
    
#Python Program to Split the array and add the first part to the end
 mylist=[1,2,3,4,5,6,7]
 firsthalf=mylist[0:4]
 secondhalf=mylist[4:]
 addtwolist=(secondhalf + firsthalf)
 print(addtwolist)

#Reverse the list
list = [1, 2, 3, 4, 5]
print("reverse list : ", original_list[::-1])

#Python Program for Find reminder of array multiplication divided by n
def findremainder(arr,n):
    mul=1
    for i in arr:
        mul=mul*i
    print(mul)
    print(mul%n)

#Find sum of array.
def findSumOfArray():
  arr = [1, 2, 3, 4, 5];
  sum = 0;
  for i in range(0, len(arr)):
    sum = sum + arr[i];
  print("Sum of all the elements of an array: " + str(sum));



findremainder([100, 10, 5, 25, 35, 14],11)
reversedlist([1, 2, 3, 4, 5,6,7,8,9]) 
findSumOfArray()  
