global_var = 'hey i am global'

class Person:
	 member_var = 5

	 def __init__(self, my_val):
	 	print(f'[INFO] This is my constructor definition')
	 	self.born_var = my_val

	 def __del__(self):
	 	print(f'[INFO] This my destructor defintion')

	 # self is compulsory arg in definition which represents scope of class
	 def set_name(self, first_name, last_name):
	 	self.first_name = first_name
	 	self.last_name = last_name
	 	self.member_var = 100

	 def show_name(self):
	 	print(f'In show_name: {self.first_name} {self.last_name}')
	 	print(f'Trying to access born_var = {self.born_var}')
	 	print(f'Access class attribute variable member_var = {self.member_var}')
	 	print(f'can i see global: {global_var}')
	 	# self is compulsory to access the other attributes of class


name = Person(50)  # Creating object (also called instance) of Person class
print(dir(name))  
print(f'name.__class__ = {name.__class__}')
# member = property = attributes all are called for the class

print(f'name.member_var = {name.member_var}')

name.set_name("Albert", "Einstein")
name.member_var = 200
name.show_name()
del name

name1 = Person(150)
name1.set_name("Narendra", "Modi")
name1.show_name()

