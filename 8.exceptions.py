# when try block fails, program goes to except block
# when try succeed, else is executed, (except will not execute)
# when except is executed, else will never execute
# finally always executes at the end
# try and except are compulsory
# else and finally are optional things

try:
	print('In try block')
	import time
	# import numpy

	# create user defined exceptions
	raise Exception("my personal error !!!!")

# except ImportError as e:
# 	print(f'io exception occured = {e}')
except Exception as e:
	print('In Except block because try failed')
	print(f'Exception info: {e}')
else:
	x = 0
	y = x + 1
	print(f'y = {y}')
	print('try successful')
	print(f'In else block, because try was successful')

finally:
	print(f'In finally block always executes at the end')


# Importance of Else:
'''
- we should write code only which can cause exception in try e.g import numpy
- if we write other than that, it may cause accidental handling of exception
e.g. NameError: name 'x' is not defined
'''
