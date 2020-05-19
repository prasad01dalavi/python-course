print("Hello World!")

# data = input("Enter your data:")
# input converts any type of input data into string type

a = 1
b = 3.14
c = "hello"

# Duck Typing
print("a variable type: ", type(a))
print("b variable type: ", type(b))
print("c variable type: ", type(c))

print('address of a', id(a))
print('address of b', id(b))
print('address of c', id(c))

# ----------------- Number ---------------------------
a = 1
b = 3.14

print(f'a = {a} | type = {type(a)}')
print(f'b = {b} | type = {type(b)}')

# ------------------ Data Type --------------- #
data_types = """
1. Number
2. List
3. Tuple
4. String
5. Sets
6. Dictionary
"""
print(data_types)
new_list = [1, "hello", 3.14, 4]  # List can hold different data type
print("new_list =", new_list)

# List inbuilt Methods
my_list = [1, 2]  # List Declaration
my_list.append(3)  # Adding 1 to list
my_list.append(4)  # Adding 2 to list
print("my_list =", my_list)

another_list = ["a", "b", "c"]
my_list.extend(another_list) 
print("extended my_list =", my_list)  # similar to my_list + another_list

my_list.remove("b")
print("after removing b =", my_list)

print('Length of list =', len(my_list))

# Slicing in List
a = [1, 'hello', 3.14, 4, 5]
print(f'a = {a}')  # all elements
print(f'a[:] = {a[:]}') # all elements
print(f'a[1:] = {a[1:]}')  # from index=1 to the last 
print(f'a[::2] = {a[::2]}')  # skip 2-1=1 element
print(f'a[:-1] = {a[:-1]}')  # from start to -1-2=-2 index 
print(f'a[-2] = {a[-2]}')  # second last element
# print(a[-6]) # gives list index out of range error
print(f'a[1:4] = {a[1:4]}')  # start from index 1 and end at index 4-1
print(f'a[1:-3+1] = {a[1:-3+1]}')  # start from index 1 and end at index -3+1=-2-1=-3  


# ----------------- Tuple ---------------------------
tup1 = (1, 'hello', 3.14, 5)
print(f'tup1 = {tup1}')
print(f'Length of tup1 = {len(tup1)}')
tup2 = (32)
print(f'tup2 = {tup2}')
print(f'type of tup2 = {type(tup2)}')

tup3 = (32,)
print(f'tup3 = {tup3}')
print(f'type of tup3 = {type(tup3)}')

print(f'tup1[2] = {tup1[2]}')
print(f'tup1[1:-1] = {tup1[1:-1]}')

print(f'tup1 + tup3 = {tup1 + tup3}')
del tup3

# ----------------- String ---------------------------
s1 = "this is my string"
s2 = 'this is my another string'
s3 = """this is also my string"""
print(f's1 = {s1} | type of s1 = {type(s1)}')
print(f's2 = {s2} | type of s2 = {type(s2)}')
print(f's3 = {s3} | type of s3 = {type(s3)}')

s4 = 'I am single quoted string, aren\'t I?'
print(f's4 = {s4}')

a = "hello "
b = "world"
print(f'a + b = {a + b}')

num = 100
print(f'a + str(num) = {a + str(num)}')

# String inbuilt functions	
print(f'Length of a = {len(a)}')

s5 = "value1,value2,value3"
comma_seperated_values = s5.split(",")
print(f'comma_seperated_values = {comma_seperated_values}')

clean_s5 = s5.replace(",", "")
print(f'clean_s5 = {clean_s5}')

name_list = ["Amar", "Akbar", "Anthony"] 
joined_names1 = name_list[0] + name_list[1] + name_list[2]
print(f'joined_names1 = {joined_names1}')

joined_names2 = ''.join(name_list)
print(f'joined_names2 = {joined_names2}')  # AmarAkbarAnthony

name_comma_string = ','.join(name_list)
print(f'name_comma_string = {name_comma_string}')

# ----------------- Sets ---------------------------
name = set({1, 'hello'})
print(f'name = {name}')
name.add(3.14)
name.add(4)
name.add('world')
name.add(4)
print(name)

a = [1, 2, 3, 2, 1, 5]
print(f'single list = {list(set(a))}')

# ----------------- Dictionary ---------------------------
dict_variable = {'name': "albert", 'age': 10, "class": 'First'}
print(f'dict_variable = {dict_variable}')

print(dict_variable['name'])
print(dict_variable['age'])

# Functions
print(len(dict_variable))
items = dict_variable.items()
print(f'items = {items}')
keys = dict_variable.keys()
values = dict_variable.values()
print(keys, type(keys))
# print(keys[0]) # not possible because of not subscriptable
dict_variable['name'] = 'Newton'

for key, value in dict_variable.items():
    print(f'{key} = {value}')


