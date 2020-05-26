class Human:
	def say_hello(self, name=None):
		if name is not None:
			print(f'Hello {name}!')
		else:
			print(f'Hello!')



obj = Human()
obj.say_hello()  
obj.say_hello("Guido")
# method overloading is happened at the end
# i.e. same method is called but with different parameter
