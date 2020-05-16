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

