#1.Write a function to check whether a person is eligible for voting or not.(accept age from user)
def age_vote(age):
    if age >= 18:
         return True
    else:
        return False

def age_validation(age):
    if age.isnumeric():
        age = int(age)
        if age < 120:
            return age
    else:
        return False
        
while(1):
    try:
        person_age= input("enter the age")
        age_valid  = age_validation(person_age)
        
        if age_valid:
            response  = age_vote(age_valid)
            
            if response == True:
                 print ("Person is eligible to vote")
        else:
             print ("Not eligible or not valid age input")

    except Exception as e:
        print("something  went wrong ", str(e))

    
#2.Write a function to check whether a number entered by user is even or odd
def even_num(num)
    if num%==0:
        return True
    else:
        return False
def num_validation(num):
    if num.isnumeric():
        num = int(num)
            return num
    else:
        return False
while(1):
    try:
        num=input("enter the number"))
        num_valid=num_validation(num)
            if num_valid:
                result=even_num(num)
                if result==True:
                    print("Number is even")
            else:
                print("Number is odd")
    
    except Exception as e:
        print("something  went wrong ", str(e))

    
#3.Write a function to check whether a number is divisble by 7 or not
def division_sev(num):
    if num%7== 0:
         return True
    else:
        return False

def num_validation(num):
    if num.isnumeric():
        num= int(num)
        return num
    else:
        return False
        
while(1):
    try:
        num1= input("enter the number")
        num_valid  = num_validation(num1)
        
        if num_valid:
            result  = division_sev(num_valid)
            
            if result == True:
                 print ("Number is divisible by 7")
            else:
                print ("Number is  not divisible by 7")
        else:
            print("enter valid input")
    except Exception as e:
        print("something  went wrong ", str(e))
    

#4.Write a function to display "Hello" if a number entered by user is multiple of five,otherwise print "Bye"
def greet(num):
    if num%5== 0:
         return True
    else:
        return False

def num_validation(num):
    if num.isnumeric():
        num= int(num)
        return num
    else:
        return False
        
while(1):
    try:
        num1= input("enter the number")
        num_valid  = num_validation(num1)
        
        if num_valid:
            result  = greet(num_valid)
            
            if result == True:
                 print ("Hello")
            else:
                print ("Bye")
        else:
            print("enter valid input")
    except Exception as e:
        print("something  went wrong ", str(e))


#5.Write a function to calculate the electricity bill according to following criteria:(100 units-free,next 100 units rs.5 per unit ,next 200 units rs.10 per units
def electric_bill(unit):
    if unit<=100:
        price=0
        return price
    elif(unit>100 and unit<=200):
        price=(unit-100)*5
        return price
    elif(unit>200):
        price=(100)*5+((unit-200)*10)
        return price
    else:
        return False

def unit_validation(unit):
    if unit.isnumeric():
        unit= int(unit)
        return unit
    else:
        return False
        
while(1):
    try:
        unit1= input("enter the numbe of units")
        unit_valid  = unit_validation(unit1)
        
        if unit_valid:
            print(unit_valid)
            result  = electric_bill(unit_valid)
            print("Bill Amount:",result)
        else:
            print("enter valid input")
    except Exception as e:
        print("something  went wrong ", str(e))


#6.write a function to display the last digit of a number
def last_digit(num):
    digit=num%10
    return digit
    
def num_validation(num):
    if num.isnumeric():
        num = int(num)
        return num
    else:
        return False
while(1):
    try:
        num1=input("enter the number")
        num_valid=num_validation(num1)
        if num_valid:
            result=last_digit(num_valid)
            print(result)
        else:
            print("enter valid input")
    except Exception as e:
        print("something  went wrong ", str(e))


#7.Write a function to check whether the last digit of a number is divisible by 3 or not
def division_three(num):
    if num%3== 0:
         return True
    else:
        return False

def num_validation(num):
    if num.isnumeric():
        num= int(num)
        return num
    else:
        return False
        
while(1):
    try:
        num1= input("enter the number")
        num_valid  = num_validation(num1)
        
        if num_valid:
            result  = division_three(num_valid)
            
            if result == True:
                 print ("Number is divisible by 3")
            else:
                print ("Number is  not divisible by 3")
        else:
            print("enter valid input")
    except Exception as e:
        print("something  went wrong ", str(e))