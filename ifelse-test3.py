#1.Write a program to check whether the number entered is three digit or not
num=int(input("Enter the number:"))
if num>99 and num<1000:
    print("The number entered is 3 digit number")
else:
    print("The number entered is  not 3 digit number")
    

#2.write a program to check whether the person is eligible to voting or not
age=int(input("Enter the age"))
if age>=18:
    print("The person is eligible to vote")
else:
    print("The person is  not eligible to vote")
    

#3.Write a program to check Whether the person is senior citizen or not
age=int(input("Enter the age"))
if age>=60:
    print("Senior Citizen")
else:
    print("Not Senior Citizen")
    
    
#4.write a program to find the lowest number out of two numbers excepted from the user
a=int(input("enter the number1:"))
b=int(input("enter the number2:"))
if a>b:
    print("The Smallest Number is:",b)
else:
    print("The Smallest Number is:",a)
    
#5.write a program to find the greatest number out of two numbers excepted from the user
a=int(input("enter the number1:"))
b=int(input("enter the number2:"))
if a>b:
    print("The greatest Number is:",a)
else:
    print("The greatest Number is:",b)
    
    
#6.Write a program to check whether the number is positive or negative
num=int(input("enter the number:"))
if num>0:
    print("The Number is Positive")
else:
    print("The Number is Negative")
    
    
#7.write a program to check whether the number is even or odd
num=int(input("enter the number"))
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")
    
    
#8.Write a program to check whether a number is divisible by 2and 3 both
num=int(input("enter the number:"))
if num%2==0 and num%3==0:
    print("The Number is divisible by 2 and 3")
else:
    print("The Number is  not divisible by 2 and 3")
    
    
#9.Write a program to find the largest number out of three numbers
a=int(input("enter the number1:"))
b=int(input("enter the number2:"))
c=int(input("enter the number3:"))
if a>b and a>c:
    print("The  Greater Number:",a)
elif b>a and b>c:
    print("The  Greater Number:",b)
else:
    print("The  Greater Number:",c)
