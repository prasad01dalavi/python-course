my_list = [1, 2, 3, 4, 5]

for element in my_list:
    print(element)
    if element == 3:
        print("in break")
        break  # break the loop (not if) instantly

for element in my_list:
    if element == 4:
        continue # continue to the next iteration directly
    print(element)

for index in range(len(my_list)):
    print(index, my_list[index])
    if my_list[index] == 3:
        print(my_list[index-1])

for index, element in enumerate(my_list):
    print('enumerated result', index, element)

# when we want index, go with enumerate
# when we do not need index, simple approach is fine

# range function
print(type(range(10)))  # list
print('range(10) = ', range(10))
for _ in range(10):
    print('hello')

# _ means dont care about this variable
# we use _ when we dont need to use variable in iteration

print(range(0, 11)[::2])
for num in range(0, 11, 2):
    print(num)
print('-----')
for num in range(10, 5, -2 ):
    print(num)
print('------ while loop below---')
# while loop
my_var = 1
while my_var <= 10:
    print(my_var)
    # my_var = my_var + 1
    if my_var == 5:
        break
    my_var += 1


# printing my_list using while
print('my list while loop')
index = 0
while index < len(my_list):
    print('element =', my_list[index])
    index += 1

