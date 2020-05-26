class Parent:
	def my_method1(self):
		print('this is my parent class my_method1')

	def my_method2(self):
		print('this is my parent class my_method2')

class Child(Parent):
	# my method2 will be overriding parent my_method2
	def my_method2(self):
		print('this is my "child" class my_method2')


child_object = Child()
child_object.my_method1()
child_object.my_method2()