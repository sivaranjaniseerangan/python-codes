#1.Write a Python program to convert a string to a list
str1="Hello World Python"
print(list(str1.split()))


#2.Write a Python program to count integer in a given mixed list. 
list1=[1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
list2=[]
for i in list1:
    if isinstance(i,int):
        list2.append(i)
print("Integrt count:",len(list2))


#3.Write a Python program to remove a specified column from a given nested list. 
Nested_list=[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print(len(Nested_list))
for i in range(0,3):
   del Nested_list[i][0]
print(Nested_list)

#4. Write a Python program to extract a specified column from a given nested list. 
list1=[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
extract_column=[]
for i in range(0,3):
    res=list1[i].pop(2)
    extract_column.append(res)
print(extract_column)


#5.Write a Python program to check if the elements of a given list are unique or not.
list1=[1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
print("Is Unique or Not")
if len(list1) > len(set(list1)):
    print("True")
else:
    print("False")
    
    
#6. Write a Python program to reverse strings in a given list of string values.
list1=['Red', 'Green', 'Blue', 'White', 'Black']
reverse_list=[]
for i in list1:
    a=i[::-1]
    reverse_list.append(a)
print("Reverse list:",reverse_list)


#7.. Write a Python program to find the maximum and minimum product from the pairs of tuple within a given list.
list1=[(2, 7), (2, 6), (1, 8), (4, 9)]
lis=[]
for i in list1:
    a=i[0]*i[1]
    lis.append(a)
print("Min_value:",min(lis),",Max_value:",max(lis))


#8.Write a Python program to find the difference between two list including duplicate elements.
lis1=[1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
lis2=[1, 1, 2, 4, 5, 6]
res=list(lis1)
for i in lis2:
    res.remove(i)
print("Difffernce between list:",res)


#9.Write a Python program to iterate over all pairs of consecutive items in a given list.
l1=[1, 1, 2, 3, 3, 4, 4, 5]
l2=[]
for i in range(len(l1)-1):
    e1=l1[i]
    e2=l1[i+1]
    pair=(e1,e2)
    l2.append(pair)
print("Consecutive pair:",l2)


#10.Write a Python program to remove the specific item from a given list of lists. 
l1=[['Red', 'Maroon', 'Yellow', 'Olive'], ['#FF0000', '#800000', '#FFFF00', '#808000'], 
['rgb(255,0,0)', 'rgb(128,0,0)', 'rgb(255,255,0)', 'rgb(128,128,0)']]
l2=[]
for i in l1:
    del i[0]
    l2.append(i)
print(l2)


#11.Write a Python program to find the maximum and minimum value of the three given lists. 
l1=[2, 3, 5, 8, 7, 2, 3]
l2=[4, 3, 9, 0, 4, 3, 9]
l3=[2, 1, 5, 6, 5, 5, 4]
list_min=min(l1+l2+l3)
list_max=max(l1+l2+l3)
print("Maximun value:",list_max)
print("Minimum Value:",list_min)


#12.Write a Python program to remove all strings from a given list of tuples.
l1=[(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]
l2=[]
for i in l1:
    print(i)
    v=list(i)
    print(v)
    for j in v:
        if isinstance(j,str):
            v.remove(j)
        print(tuple(v))
    l2.append(tuple(v))
print("After Removing String:",l2)


#13.Write a Python program to find the dimension of a given matrix.
l1=[[0, 1, 2], [2, 4, 5], [2, 3, 4]]
row=len(l1)
column=len(l1[0])
print("Dimension:",row,column)


#14.Write a Python program to initialize and fills a list with the specified value. 
n=3
val=8
lis=[]
for i in range(8):
     lis.append(3)
print("fill_list:",lis)

#15.Write a Python program to create a given flat list of all the keys in a flat dictionary. Go to the editor
dict={'Laura': 10, 'Spencer': 11, 'Bridget': 9, 'Howard ': 10}
print(list(dict.keys()))


#16.Write a Python program to get the most frequent element in a given list of numbers. Go to the editor
lis=[2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]
print(lis.count)
max1=max(set(lis),key=lis.count)
print(max1)


#17.Write a Python program to generate a list, containing the Fibonacci sequence, up until the nth term. 
n=7
seq=[0,1]
if n<=0:
    print("res:",0)
while len(seq)<=n:
    val=seq[len(seq) - 1] + seq[len(seq) - 2]
    seq.append(val)
print("Fibanacci Series:",seq)


#18.Write a Python program to check if there are duplicate values in a given flat list.
l1=[1, 2, 3, 4, 5, 6, 7,8,8]
set1=set(l1)
if len(l1)==len(set1):
    print(True)
else:
    print(False)
    

#19.Write a Python program to count lowercase letters in a given list of words
l1=["Red", "Green", "Blue", "White"]
sum1=0
for i in l1:
    for j in i:
        print(j)
        sum1+=j.islower()
print("count_lower:",sum1)


#20.Write a Python program to calculate the sum of two lowest negative numbers of a given array of integers
l1=[-14, 15, -10, -11, -12, -13, 16, 17, 18, 19, 20]
l2=sorted(l1)
print("sum:",l2[0]+l2[1])


    

    

        