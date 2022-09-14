#1.Write a Python script to sort (ascending and descending) a dictionary by value
dict1 = {'a':1,'b':10,'c':16,'d':9}
sorted_values = sorted(dict1.values()) 
print(sorted_values )
sorted_dict = {}

for i in sorted_values:
    for k in dict1.keys():
        if dict1[k] == i:
            sorted_dict[k] = dict1[k]
            print(sorted_dict[k])
            break
print(sorted_dict)


#2.Write a Python script to add a key to a dictionary.
update_dict={0: 10, 1: 20}
update_dict[2]=30
print(update_dict)


#3.Write a Python script to concatenate following dictionaries to create a new one
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)


#4. Write a Python script to check whether a given key already exists in a dictionary
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
print (49 in squares)


#5.Write a Python program to iterate over dictionaries using for loops
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
for key in a_dict:
    print(key)
for item in a_dict.items():
    print(item)
for value in a_dict.values():
    print(value)
    
    
#6. Write a Python program to get the maximum and minimum value in a dictionary.
ages = {'Matt': 30,'Katie': 29,'Nik': 31,'Jack': 43,'Alison': 32,'Kevin': 38}
print("min value:",min(ages.values()))
print("max value:",max(ages.values()))

#7. Write a Python program to remove duplicates from Dictionary
ages = {'Matt': 30,'Katie': 29,'Nik': 31,'Jack': 43,'Alison': 32,'Kevin': 38,'Jack': 43,'Alison': 32,'Kevin': 38}
result={}
for key,value in ages.items():
    if value not in result.values()
        result[key] = value
print(result)


#8. Write a Python program to sort a given dictionary by key
color_dict = {'red':'#FF0000','green':'#008000','black':'#000000', 'white':'#FFFFFF'}
print(sorted(color_dict.items()))


#9.Write a Python program to combine two dictionary adding values for common keys
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
for key in d2:
    if key in d1:
        d2[key]=d1[key]+d2[key]
    else:
        pass
    print(d2[key])
d1.update(d2)
print(d1)

#10.Write a Python program to print all unique values in a dictionary.
sam_dict= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
list1=[]
for dic in  sam_dict : 
    print(dic)
    for key in dic:
        a=dic[key]
        list1.append(a)
        print(list1)
s1=set(list1)
print(s1)


