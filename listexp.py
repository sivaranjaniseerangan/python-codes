#1.Write a Python program to sum all the items in a list.
list1=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in range(len(list1)):
    sum=sum+list1[i]
print("Sum of list:",sum) 


#2. Write a Python program to multiply all the items in a list.
list1=[1,2,3,4,5]
multiply=1
for i in range(len(list1)):
    multiply=multiply*list1[i]
print(" multiplication of list:",multiply) 


#3.Write a Python program to get the largest number from a list
list1=[1,2,3,4,5,6,7,8,9,10]
print(list1)
print(max(list1))


#4.Write a Python program to remove duplicates from a list.
list1=[10,10,15,20,20,25,30,30,35,40,40]
set1=set(list1)
print(list(set1))

#5.Write a Python program to check a list is empty or not.
list1=[1,2]
if len(list1) == 0:
    print("The list is empty")
else:
    print("The list is not empty")
    
    
#6.Write a Python program to clone or copy a list
list1=[1,2,3,4,5,6,7,8,9,10]
list2=list1
list3=list1.copy()
list1.append(11)
print(list1,list2,list3)


#7.Write a Python program to extend a list without append
list1=[10, 20, 30]
list2=[40, 50, 60]
list1.extend(list2)
print(list1)


#8.Write a Python program to print a specified list after removing the 0th, 4th and 5th elements
list1= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
list1.pop(5)
list1.pop(4)
list1.pop(0)
print(list1)

#9.Write a Python program to shuffle and print a specified list
import random
list1=[1,2,3,4,5,6,7,8,9,10]
random.shuffle(list1)
print(list1)

#10.Write a Python program to print the numbers of a specified list after removing even numbers from it.
list1=[1,2,3,4,5,6,7,8,9,10]
for i in list1:
    if i%2==0:
       print(i)
       list1.remove(i)
else:
    print(list1)


