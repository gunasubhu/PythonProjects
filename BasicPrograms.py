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

def factorial_of_number(num1):
    fact=1
    for i in range(1,num1+1):
        fact=fact*i
    print(f"Factorial of {num1} is {fact}")

def maximum_of_two_numbers(num1,num2):
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num1==num2:
        print(f"{num1} equal to {num2}")
    else:
        print(f"{num2} is greater than {num1} ")

def addtwonumbers(num1,num2):
    sum=num1+num2
    print(f"Sum of {num1}+{num2}={sum}")


findSumOfArray()   
area(4)
compound_interest(10000,6,5)
simple_interest(10000,6,6)
addtwonumbers(10,20)
maximum_of_two_numbers(50,40)
factorial_of_number(4)
