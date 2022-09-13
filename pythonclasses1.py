#1.Write a Python program to create an instance of a specified class and display the namespace of the said instance
class Student:
    def __init__(self,firstname,lastname,grade,age):
        self.firstname=firstname
        self.lastname=lastname
        self.grade=grade
        self.age=age
student=Student('John','Hendry',8,14)
print(student.__dict__)

#2.Write a Python class to convert an integer to a roman numeral.
class roman:
    def getroman(self,num):
        self.num=num
        value= [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
        symbol=["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
        roman_num=""
        print(roman_num)
        i=0 
        while num>0:
            div=num//value[i]
            num=num%value[i]
            while div:
                roman_num=roman_num+symbol[i]
                div=div-1
            i=i+1
        return roman_num
print(roman().getroman(5))


#3.Write a Python class to convert a roman numeral to an integer
class int_num:
    def get_int(self,s):
        self.str=str
        roman_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        prev_num=0
        cur_num=0
        result=0
        for i in range(len(s)):
            cur_num=roman_val[s[i]]
            if cur_num>prev_num:
                result=result+(cur_num-2*prev_num)
            else:
                result+=cur_num
            prev_num=cur_num
        return result 
print(int_num().get_int("XV"))


#4.Write a Python class to get all possible unique subsets from a set of distinct integers
class subset:
    def sub1(self,set1):
        return self.sub2([],sorted(set1))
    def sub2(self,curr,set1):
        if set1:
            return self.sub2(curr,set1[1:])+self.sub2(curr+[set1[0]],set1[1:])
        return [curr]
a=[4,5,6]
a1=[]
for i in range(0,2):
    b=a[i]
    a1.append(b)
print(subset().sub1(a))

#5.Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum 
#equals a specific target number
class pair_ele:
    def pair_two(self,n,target):
        self.n=n 
        self.target=target
    def sum_pair(self,n,target):
        for i in range(0,7):
            for j in range(i-1,7):
                if(A[i]+A[j]==target):
                    return i,j
A= [10,20,10,40,50,60,70]
get=50
print(pair_ele().sum_pair(len(A),get))
 
#6. Write a Python class to implement pow(x, n). 
class pow:
    def pow_num(self,x, n):
       
        if x==0 or x==1 or n==1:
            return x 
        if x==-1:
            if n%2 ==0:
                return 1
            else:
                return -1
        if n==0:
            return 1
        if n<0:
            return 1/self.pow_num(x,-n)
        val = self.pow_num(x,n//2)
        if n%2 ==0:
            return val*val
        return val*val*x
print("pow(x,n) value is :",pow().pow_num(3,3)) 


#7.Write a Python class to reverse a string word by word
class reverse:
    def reverse_str(self,str):
        res=str[::-1]
        return res
print(reverse().reverse_str("Hello World.py"))


#8. Write a Python class which has two methods get_String and print_String. get_String accept a string 
#from the user and print_String print the string in upper case. 
 class string:
    def __init__(self):
        self.str=""
    def get_string(self):
        str=input("enter the string")
    def print_string(self):
        print(self.str.upper())
str= string()
str.get_string()
str.print_string()


#9.. Write a Python class named Rectangle constructed by a length and width and a method which will 
#compute the area of a rectangle.
class rect():
    def __init__(self,leng,wid):
        self.leng=leng
        self.wid=wid
    def rect_area(self):
        area=self.leng*self.wid
        return area
rec_area=rect(2,4)
print(rec_area.rect_area())

#10.Write a Python class named Circle constructed by a radius and two methods which will 
#compute the area and the perimeter of a circle.
class circle():
    def __init__(self,radi):
        self.radi=radi
    def cir_area(self):
        area=3.14*self.radi**2
        return area
    def cir_peri(self):
        perm=2*3.14*self.radi
        return perm
cir_radi=circle(4)
print(cir_radi.cir_area())
print(cir_radi.cir_peri())