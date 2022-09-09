#1.Write a program to check whether a person is eligible for voting or not.(accept age from user)
person_age= int(input("enter the age"))
if person_age >= 18:
     print ("Person is eligible to vote")
else:
     print ("Not eligible")
    
 
#2.Write a program to check whether a number entered by user is even or odd
num=int(input("enter the number"))
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")
    
    
#3.Write a program to check whether a number is divisble by 7 or not
val=int(input("enter the value"))
if val%7 ==0:
    print("Number is divisible by 7")
else:
    print("Number is not divisible by 7")
    
#4.Write a program to display "Hello" if a number entered by user is multiple of five,otherwise print "Bye"
a=int(input("enter the number"))
if a%5 ==0:
    print("Hello")
else:
    print("Bye")


#5.Write a program to calculate the electricity bill according to following criteria:(100 units-free,next 100 units rs.5 per unit ,next 200 units rs.10 per units
unit=int(input("enter the units"))
if unit<=100:
    print("NO Charge")
elif(unit>100 and unit<=200):
    print("Bill Amount:",(unit-100)*5)
else:
    print("Bill Amount:",(((100)*5)+((unit-200)*10)))

#6.write a program to display the last digit of a number
value=int(input("enter the number"))
print(value%10)

#7.Write a program t0 check whether the last digit of a number is divisible by 3 or not
num=int(input("enter the number"))
a=num%10
if a%3==0:
    print("Number divisible by 3")
else:
    print("Number not divisible by 3")
