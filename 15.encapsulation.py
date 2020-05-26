'''
1. Private var can not be accessed outside of the class using object
2. Private var can not be changed outside of the class using object
'''

class MyClass:
	my_public_var = 0
	__my_private_var = 0
	# two underscore at the beginning indicates that it is private member

	def __init__(self):
		self.my_public_var = 10
		self.__my_private_var = 20

	def show_variables(self):
		print(f'my_public_var = {self.my_public_var}')
		print(f'__my_private_var = {self.__my_private_var}')

	def set_private_variables(self, value):
		self.__my_private_var = value



obj = MyClass()

# obj.my_public_var = 100  	# can be easily changed
# obj.set_private_variables(300)			
# # changing the private var using class method
# # which is allowed
# obj.show_variables()
# print(obj.my_public_var)

print(dir(obj))
obj.__my_private_var = 200  # not able to change the private variable
obj.nonsense_var = 8
print(obj.nonsense_var)
print(obj.__my_private_var)  # can not access private var outside of class

