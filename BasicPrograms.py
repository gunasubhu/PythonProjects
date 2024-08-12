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

def primenumber(n):
  #n=13
  flag=0
  endrange=n//2
  for i in range(2,endrange+1):
    if n%i==0:
      flag=1
      break
    else:
      flag=0
  if flag==0:
    print("prime number:",n)
  else:
    print("not a prime number:",n)

#How to find the highest number
a=10
b=200
c=300

if a>b and a>c:
  print(f"the highest number is: {a}")
  
elif b>c:
  print(f"the highest number is: {b}")
  
else: 
   print(f"the highest number is: {c}")

#Python program to print all Prime numbers in an Interval
def primeseries(start,end):
    for n in range(start,end):
          flag=0
          endrange=n//2
          for i in range(2,endrange+1):
            if n%i==0:
              flag=1
              break
            else:
              flag=0
          if flag==0:
            print("prime number:",n)

def fibonacciNumber(end):
    n1=0
    n2=1
    for i in range(1,end+1):
        n3=n1+n2
        n1=n2
        n2=n3
        print(n3)


#Python Program for How to check if a given number is Fibonacci number?
import math
 
def IsPerfectSquare(n):
    sqrt_num = math.sqrt(n)
    if sqrt_num.is_integer():
        return True
    else:
        return False
        
# val=IsPerfectSquare(25)  
# print(val)

def IsFibonacciNumber(n):
    n1=(5*(n**2))+4
    n2=(5*(n**2))-4
    
    p1=IsPerfectSquare(n1)
    p2=IsPerfectSquare(n2)
    if p1==True or p2==True:
        print(f"{n} is a fibonacci number")
    else:
        print(f"{n} is not a fibonacci number")

#student marks and status:
def FindtheStudentMarks(mark):
    if mark>=450 and mark<=500:
        print("O grade")
    elif mark>=400 and mark<=449:
        print("A grade")
    elif mark>=350 and mark<=399:
        print("B grade")
    elif mark>=300 and mark<=349:
        print("C grade")
    elif mark>=250 and mark<=299:
        print("D grade")
    elif mark<250:
        print("Fail")
    elif mark>500:
        print("Invalid number")


def studentMarks(mark):
    if mark>=80 and mark<=100:
        return "Distinction"
    elif mark>=60 and mark<=79:
        return "First class"
    elif mark>=50 and mark<=59:
        return "Second class"
    elif mark>=35 and mark<49:
        return "Third class"
    elif mark<35:
        return "Fail"
    elif mark>100:
        return "Invalid"
        
#Get the student mark details
def studentDetails(name,mark1,mark2,mark3,mark4,mark5):
    print("Student name:",name)
    total_marks=(mark1+mark2+mark3+mark4+mark5)
    print("Total marks:", total_marks)
    Tamil=studentMarks(mark1)
    English=studentMarks(mark2)
    Maths=studentMarks(mark3)
    Science=studentMarks(mark4)
    SocialScience=studentMarks(mark5)
    print(f"Tamil mark: {mark1}, Class: {Tamil}")
    print(f"English mark: {mark2}, Class: {English}")
    print(f"Maths mark: {mark3}, Class: {Maths}")
    print(f"Science mark: {mark4}, Class: {Science}")
    print(f"Social Science mark: {mark5}, Class: {SocialScience}")
    
    overallstatus='Pass'
    if Tamil=='Fail' or Tamil=='Invalid':
        overallstatus='Fail'
    elif English=='Fail' or English=='Invalid':
        overallstatus='Fail'    
    elif Maths=='Fail' or Maths=='Invalid':
        overallstatus='Fail'
    elif Science=='Fail' or Science=='Invalid':
        overallstatus='Fail'
    elif SocialScience=='Fail' or SocialScience=='Invalid':
        overallstatus='Fail'
    else:
        overallstatus='Pass'
    
    print("Overall Status:",overallstatus)

#Banck account transactons(Deposit,Withdrawal)
def AccountMaintanance(name,balance,transactiontype,transactonAmount):
    message =''    
    if transactiontype=="deposit":#Comparisson operator
        Currentbalance=balance+transactonAmount
        message="Amount deposited successfully"
    elif transactiontype=="withdrawal":
        if transactonAmount>balance:
            message="Insuffient fund"
        else:
            Currentbalance=balance-transactonAmount
            message="Withdrawal successfully"
            if Currentbalance<1000:
                 message=message+". Please maintain the minimum balance amount"
    else:
        Currentbalance=balance
        message="Invalid transaction"
        
    print("Account holder name:",name)
    print("Account balance is:",balance)
    print("Transaction Type:",transactiontype)
    print("Transaction Amount:",transactonAmount)
    print("Current balance:",Currentbalance)
    print("Transaction messsage:",message)


#Python Program for Sum of squares of first n natural numbers.
def Sumofsquares(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i*i
    print(f"Sum of squares of first {n} natural numbers: {sum}")

#Python Program for cube sum of first n natural numbers
def cubenumber(n):
    sum=0
    for i in range(1,5+1):
        sum=sum+i*i*i
    print(f"cube sum of first {n} natural numbers: {sum}")


def studentMarks(mark):
    if mark>=80 and mark<=100:
        return "Distinction"
    elif mark>=60 and mark<=79:
        return "First class"
    elif mark>=50 and mark<=59:
        return "Second class"
    elif mark>=35 and mark<49:
        return "Third class"
    elif mark<35:
        return "Fail"
    elif mark>100:
        return "Invalid"
        
#Get the student mark details using array program.
def studentDetails(name,marks):
    print("Student name:",name)
    total_marks=sum(marks)
    print("Total marks:", total_marks)
    Tamil,English,Maths,Science,SocialScience=marks
    print(f"Tamil mark: {Tamil}, Class: {studentMarks(Tamil)}")
    print(f"English mark: {English}, Class: {studentMarks(English)}")
    print(f"Maths mark: {Maths}, Class: {studentMarks(Maths)}")
    print(f"Science mark: {Science}, Class: {studentMarks(Science)}")
    print(f"Social Science mark: {SocialScience}, Class: {studentMarks(SocialScience)}")
    
    overallstatus='Pass'
    if Tamil=='Fail' or Tamil=='Invalid':
        overallstatus='Fail'
    elif English=='Fail' or English=='Invalid':
        overallstatus='Fail'    
    elif Maths=='Fail' or Maths=='Invalid':
        overallstatus='Fail'
    elif Science=='Fail' or Science=='Invalid':
        overallstatus='Fail'
    elif SocialScience=='Fail' or SocialScience=='Invalid':
        overallstatus='Fail'
    else:
        overallstatus='Pass'
    
    print("Overall Status:",overallstatus)

#Reverse the list
def reversedlist(num):
 
    num2 = []
    for i in num:
        print(i,[i],num2)
        num2 = [i] + num2
    print("reversed list : ", num2)
    



#Reverse the list
list = [1, 2, 3, 4, 5]
print("reverse list : ", original_list[::-1])
    
reversedlist([1, 2, 3, 4, 5,6,7,8,9]) 
studentDetails("Ranjith",[50,70,65,90,60])        
cubenumber(5)
Sumofsquares(4)  
AccountMaintanance("Ranjith",10000,"withdrawal",9500)   
studentDetails("Ranjith",50,70,65,90,60)
FindtheStudentMarks(-5)                
IsFibonacciNumber(33)      
fibonacciNumber(10)
primeseries(2,100)
primenumber(13)
findSumOfArray()   
area(4)
compound_interest(10000,6,5)
simple_interest(10000,6,6)
addtwonumbers(10,20)
maximum_of_two_numbers(50,40)
factorial_of_number(4)
