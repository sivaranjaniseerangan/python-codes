#1.Write a program to accept the percentage from the user and display the grades according to the following criteria:
percent=int(input("enter the percentage"))
if percent>90:
     print("Grade:A")
elif percent>80 and percent <=90:
    print("Grade:B")
elif percent>=60 and percent<=80:
    print("Grade:C")
else:
    print("Grade:D")

#2.Write a program to accept the cost price of a bike and display the raod tax to be paid according to the following criteria:
cost=int(input("enter the cost of bike"))
if cost>100000:
    print("Tax 15%:",(15/100)*cost)
elif cost>50000 and cost<=100000:
    print("Tax 10%:",(10/100)*cost)
else:
    print("Tax 5%:",(5/100)*cost)

#3.Write a program to check whether an leap year or not
year=int(input("enter the year"))
if year%4 == 0:
    print("leap year")
else:
    print("Not a leap year")

#4.Write a program to accept a number from 1 to 7 and display the name of the weeks
num=int(input("Enter number from 1 to 7:"))
if num==1:
    print("Sunday")
elif num==2:
    print("Monday")
elif num==3:
    print("Tuesday")
elif num==4:
    print("Wednesday")
elif num==5:
    print("Thursday")
elif num==6:
    print("Friday")
else:
    print("Saturday")


#5.Write a program to accept a number from 1 to 12 to display months and no of days
num=int(input("Enter number from 1 to 12:"))
if num==1:
    print("January,Number of days-31")
elif num==2:
    print("February,Number of days-28 or 29")
elif num==3:
    print("March,Number of days-31")
elif num==4:
    print("April,Number of days-30")
elif num==5:
    print("May,Number of days-31")
elif num==6:
    print("June,Number of days-30")
elif num==7:
    print("July,Number of days-31")
elif num==8:
    print("August,Number of days-31")
elif num==9:
    print("September,Number of days-30")
elif num==10:
    print("October,Number of days-31")
elif num==11:
    print("November,Number of days-30")
else:     
    print("December,Number of days-31")
    
    
#6.write a program to accept city from the user and display monument of that city
city=input("enter the city")
if city == "Delhi":
    print("Monument of the city:Red Fort")
elif city == "Agra":
    print("Monument of the city:Taj Mahal")
elif city =="Jaipur":
    print("Monumet of the city:Jal Mahal")
else:
    print("Enter the correct city")