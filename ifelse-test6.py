#1.Accept the three numbers from the user and display the second largest number
a=int(input("Enter the number1:"))
b=int(input("Enter the number2:"))
c=int(input("Enter the number3:"))
if (a>b and a<c) or (a<b and a>c):
    print("The second largest number is:",a)
elif(b>c and b<a) or (b<c and b>a):
    print("The second largest number is:",b)
else:
     print("The second largest number is:",c)

#2.Accept three sides of a triangle and check whether traingle is possible or not
a=int(input("Enter the first side of triangle:"))
b=int(input("Enter the second side of triangle:"))
c=int(input("Enter the third side of triangle:"))
if a+b>c or b+c>a or a+c>b:
    print("Triangle is possible")
else:
    print("Triangle is not possible")
    
    
#3.Accept the electric units from the user and calculate the bill
unit=int(input("enter the units"))
if unit<=100:
    print("Free")
elif(unit>100 and unit<=300):
    print("Bill Amount:",(unit-100)*2)
else:
    print("Bill Amount:",(400+(unit-300)*5))
    
    
#4.Accept the no of days from the user and calculate the library charges
days=int(input("Enter the number of days"))
if days<=5:
    print("Charges:",days*2)
elif days>=6 and days<=10:
    print("Charges:",days*3)
elif days>=11 and days<=15:
    print("Charges:",days*4)
else:
    print("Charges:",days*5)


#5.Accept the kilometers covered and calulate the bill
km=int(input("Enter the kiometers covered"))
if km<=10:
    print("Bill Amount:",km*11)
elif km<=100:
    print("Bill Amount:",((10*11)+((km-10)*10)))
else:
    print("Bill Amount:",(1010+(km-100)*9))

#6.accept the marks and display the stream accordingly
eng=int(input("Enter the english marks"))
math=int(input("Enter the math marks"))
sci=int(input("Enter the scinece marks"))
social=int(input("Enter the social studies marks"))
if eng>80 and math>80 and sci>80 and social>80:
    print("SCience Stream")
elif eng>80 and math>50 and sci>50:
    print("Commerece Stream")
elif eng>80 and social>80:
    print("Humanities")
else:
    print("Enter the correct marks")

 
    