furits_list = ["apple", "banana", "cherry",'apple','banana','cherry']
furits_tuple = ("apple", "banana", "cherry")
furits_set = {"apple", "banana", "cherry"}
furits_dict = {"apple": 1, "banana": 2, "cherry": 3}


print('apple' in furits_list) 
print('banana' in furits_tuple)
print('cherry' in furits_set)
print('apple' in furits_dict)  

print(len(furits_list))
print(len(furits_tuple))
print(len(furits_set))
print(len(furits_dict))

for fruit in furits_list:
    print(fruit)
    
for fruit in furits_tuple:
    print(fruit)
    
for fruit in furits_set:
    print(fruit)
    
for key in furits_dict.items():
    print(key)
    


#  if we need a duplicate data we can use list or tuple
# if we need a unique data we can use set or dict
# if we need a key value pair we can use dict
# if we need fast retrieval we can use dict or set
# if we need ordered data we can use list or tuple
# if we need immutable data we can use tuple or frozenset
# if we need mutable data we can use list, set or dict
# if we need to store data with different types we can use list, tuple or dict
# if we need to store data with same types we can use set or dict

