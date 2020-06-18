import login as lg
from login import MyClass
from login import login
from login import *  # this should never be used in programming

print(MY_CONSTANT) 

# when we directly run the python file, __name__ is __main__
# when we import python file, __name__ is <name of that python file>

lg.login() # or
login()

def search(keyword):
	print(f'[INFO] Searching the keyword: {keyword}')

def chatbot(question):
	print(f'[INFO] Asking question to chatbot: {question}')


obj = MyClass()
obj.function1()

search('PW')
chatbot('Who is Accused?')