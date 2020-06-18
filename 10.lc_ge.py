# List Comprehension
# list of even numbers

even_list = []
for num in range(50):
	if num % 2 == 0:
		even_list.append(num)

print(f'even list: {even_list}')

# now above code using LC
even_lc_list = [num for num in range(50) if num % 2 == 0]

print(f'LC output: {even_lc_list}')

# another example
square_list = []
for num in range(20):
	square_list.append(num ** 2)
print(f'square list: {square_list}')

# above using LC
square_lc_list = [num**2 for num in range(2000)]
print(f'square lc output: {square_lc_list}')

# Generator Expressions
square_ge_list = (num**2 for num in range(20))
print(f'square ge list: {square_ge_list}')

# generator doesnot consume memory like List
import time
# for element in square_ge_list:
# 	print(element)
# 	time.sleep(1)  # 1 sec delay

for i in range(10):
	print(f'My number is {i}', end='\r')
	time.sleep(2)




