class Parent1:
	value1 = "this is my value1"
	value2 = "this is my value2"


class Parent2:
	value3 = "this is my value3"
	value4 = "this is my value4"


class Child(Parent1, Parent2):
	pass

parent1_object = Parent1()
print(parent1_object.value1)

child_object = Child()
print(child_object.value2)  # accessing property of parent1
print(child_object.value3)  # accessing property of parent2
