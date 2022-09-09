#1.calculate the percentage of class attened
workingdays=int(input("Enter the number of working days"))
absentdays=int(input("Enter the number of absent days"))
percentage=((workingdays-absentdays)/workingdays)*100
if percentage < 75:
    print("students will not able to write the exam")
else:
    print("students will able to write the exam")
print("percentage",percentage,"%")


#2.Accept the percentage from the user and display the grades:
percent=int(input("Enter the percentage"))
if percent>80:
    print("Grade A+")
elif percent<=80 and percent>60:
    print("Grade A")
elif percent<=60 and percent>50:
    print("Grade B+")
elif percent<=50 and percent>45:
    print("Grade B")
elif percent<=45 and percent>25:
    print("Grade C")
else:
    print("Grade D")
    
    
#3.A company decieded to give bonus according to following criteria
salary=int(input("enter the salary"))
serviceyear=int(input("enter the years of service"))
if serviceyear > 10:
    print("Net Bonus:",(10/100)*salary)
elif serviceyear <= 10 and serviceyear >= 6:
    print("Net Bonus:",(8/100)*salary)
else:
    print("Net Bonus:",(5/100)*salary)


#4.Accept the marked price from the user and calculate the net amount
markedprice=int(input("enter the marked price"))
if markedprice  > 10000:
    print("Net Amount:",markedprice-((20/100)*markedprice))
elif markedprice <= 10000 and serviceyear >= 7000:
    print("Net Amount:",markedprice-((15/100)*markedprice))
else:
    print("Net Amount:",markedprice-((10/100)*markedprice))
    
    
#5.write a program to accept the prcentage and display the category
percent=int(input("Enter the pecentage"))
if percent>=65:
    print("Excellent")
elif percent>=55 and percent<65:
    print("Good")
elif percent>=40 and percent<55:
    print("Fair")
else:
    print("Failed")
    
    
#6.Accept the three sides of a triangle and check the types:
a=int(input("Enter the first side of triangle:"))
b=int(input("Enter the second side of triangle:"))
c=int(input("Enter the third side of triangle:"))
if a=b=c:
    print("Equilateral Triangle")
elif a=b!=c or a!=b=c or a=c!=b:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
    
    
#7.Write a program to accept two numbers and mathematical oprators
a=int(input("Enter the number1:"))
b=int(input("Enter the number2:"))
sym=input("Enter the mathematical operator")
if sym=='+':
    print("sum:",a+b)
elif sym=='-':
    print("sub:",a-b)
elif sym='*':
    print("Multiply:",a*b)
elif sym='/':
    print("Division:",a/b)
elif sym='%':
    print("Mod:",a%b)
elif sym='^':
    print("Exp:",a^b)
else:
    print("Enter the valid operator")
    
    
#8.accept the age , sex and no of day and diaplay the wages accordingly
age=int(input("Enter the age"))
sex=input("Enter the sex")
days=int(input("Enter the number of days"))
if age>=18 and age<30 and sex=="M":
    print("wages:",700*days)
elif age>=18 and age<30 and sex=="F":
    print("wages:",750*days)
elif age>=30 and age<=40 and sex=="M":
    print("wages:",800*days)
elif age>=30 and age<=40 and sex=="F":
    print("wages:",850*days)
else:
    print("Enter the appropriate Age")


