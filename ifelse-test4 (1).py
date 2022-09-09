#1.Accept the temperature in celcisus of water and check whether the water is boiling or not
temp=int(input("Enter thr temperature"))
if temp>=100:
    print("The water is boiling")
else:
    print("The water is not boiling")
    
    
#2.Accept the age of four people and display the youngest one
a=int(input("Enter the age1"))
b=int(input("Enter the age2"))
c=int(input("Enter the age3"))
d=int(input("Enter the age4"))
if a<b and a<c and a<d:
    print("The age of Youngest one is",a)
elif b<a and b<c and b<d:
    print("The age of Youngest one is",b)
elif c<a and c<b and c<d:
    print("The age of Youngest one is",c)
else:
    print("The age of Youngest one  is",d)
    
    
#3.Accept the age of four people and display the oldest one
a=int(input("Enter the age1"))
b=int(input("Enter the age2"))
c=int(input("Enter the age3"))
d=int(input("Enter the age4"))
if a>b and a>c and a>d:
    print("The age of Oldest one is",a)
elif b>a and b>c and b>d:
    print("The age of Oldest one is",b)
elif c>a and c>b and c>d:
    print("The age of Oldest one is",c)
else:
    print("The age of Oldest one is",d)


#4.Write a program to check Whether the number is prime or not
num = int(input("Enter a number: "))
if num>1:
    for i in range(2,num):
        if num%i == 0:
            print("The number",num,"is not prime")
            break
    else:
            print("The number",num,"is prime")
else:
    print("The number",num,"is not prime")
    
#5.Write a program to check the character is vowel or not
a=input("Enter the Character")
vow="AEIOUaeiou"
if a in vow:
    print("The Character is Vowel")
else:
    print("The Character is  Not Vowel)
    
