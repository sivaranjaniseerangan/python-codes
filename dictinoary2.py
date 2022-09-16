#1.Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
dict1={}
n=10
for i in range(1,11):
    dict1[i]=i*i
print( "Dictionary:",dict1)


#2.Write a Python program to find the highest 3 values of corresponding keys in a dictionary.
d1={'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
dic=[]
for (key,value) in d1.items():
    d=(value,key)
    dic.append(d)
res=sorted(dic)   
print(res)
print(len(dic))
hig_dict=res[-3:]
print(hig_dict)
key1=[]
for i in hig_dict:
    a=i[1]
    key1.append(a)
print(key1)


#3.Write a Python program to convert a list into a nested dictionary of keys.
lis=[1, 2, 3, 4]
d1=d2={}
for i in lis:
    d2[i]={}
    d2=d2[i]
print(d1)


#4. Write a Python program to sort a list alphabetically in a dictionary.
d1={'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
for (i,j) in d1.items():
    d1[i]=sorted(j)
print(d1)


#5.Write a Python program to print a dictionary line by line.
d1={'Aex':{'class':'V','rolld_id':2},'Puja':{'class':'V', 'roll_id':3}}
for i in d1:
    print(i)
    for j in d1[i]:
        print(j,":",d1[i][j])


#6.Write a Python program to create a dictionary of keys x, y, and z where each key has as value a list from 
#11-20, 21-30, and 31-40 respectively. Access the fifth value of each key from the dictionary.
d1=dict(x=list(range(11,20)),y=list(range(21,30)),z=list(range(31,40)))
print(d1)
print("Fifth Element:",d1["x"][4])
print("Fifth Element:",d1["y"][4])
print("Fifth Element:",d1["z"][4])


#7.Write a Python program to check all values are same in a dictionary.
d1={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
v1=list(d1.values())[0]
res=True
for  key in d1:
    dval=d1[key]
    if dval !=v1:
        res=False
        break
print(res)


#8.Write a Python program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists. 
d1=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
res={}
for i,j in d1:
    res.setdefault(i,[]).append(j)
print(res)


#9.Write a Python program to remove a specified dictionary from a given list. Go to the editor
d1=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, 
{'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
rem_id="#FF0000" 
for i in range(len(d1)):
    if d1[i]['id'] == rem_id:
        del d1[i]
        break
print(d1)


#10.Write a Python program to convert string values of a given dictionary, into integer/float datatypes.
l1=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
for dic in l1:
    for k1 in dic:
        dic[k1] = int(dic[k1])
print(l1)