from datetime import datetime

MY_CONSTANT = 23

def login():
	print(f'[INFO] Login Successful!')
	return datetime.now()


class MyClass:
	def function1(self):
		print(f'[INFO] Function 1 is called!')

	def function2(self):
		print(f'[INFO] Function 2 is called!')

print(f'[INFO] In Login module __name__ = : {__name__}')

if __name__ == '__main__':
	# whatever comes in this if condition, will not be executed when module is
	# imported
	print(f'[INFO] Module is directly run!')
	login()
	MyClass().function1()



