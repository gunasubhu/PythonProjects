import math

def simple_interest(p,r,t):
    result=(p*r*t)/100

    print(f"{p},{r},{t}={result}")#Simple interest is:", result)



def compound_interest(principal,rate,time):
  Amount=principal
  for i in range(time):
    Amount=Amount*(1+rate/100)
  CI=Amount-principal
  p=round(principal)
  print(f"Amount {principal}-principal {Amount}=Compountinterest {CI}")


def area(r):
  area = math.pi* pow(r,2)
  print('Area of circle is:' ,area)

def findSumOfArray():
  arr = [1, 2, 3, 4, 5];
  sum = 0;
  for i in range(0, len(arr)):
    sum = sum + arr[i];
  print("Sum of all the elements of an array: " + str(sum));

findSumOfArray()   
area(4)
compound_interest(10000,6,5)
simple_interest(10000,6,6)
