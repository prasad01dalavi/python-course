# 1. function definition
# 2. function call


# function definition
def func():
    print('this is my function')


func()  # function call

new_func = func
new_func()

def calc(a, b, c=4):  # here c is default optional argument
    addition = a + b + c
    subtraction = a - b - c
    return addition, subtraction, a*b*c
    # number of return vars and catching vars should(not must) be same

result = calc(10, 5, 3)
print('returned result = ', result)

# args (variable length argumentss) and kwargs 
def foo(required,  *args, **kwargs):
    print('required ', required)
    if args:
        print('args:', args)
    if kwargs:
        print('kwargs:', kwargs)
        print('first key value = ', kwargs['key1'])

foo('hello', 'new', 4, 5, 6, key1='value1', key2='value2')


def bar(*args):
    print('my limitless args:', args)

bar(1,2,3,'hey', 'good')


def sum(arg1, arg2):return arg1 + arg2
print(f'sum = {sum(2,4)}')

# lambda is called anonymous function
# lambda is an expresssion
add = lambda arg1, arg2: arg1 + arg2
print(f'lambda result = {add(4, 5)}')


var = 100  # global variable
print(id(var))
def function1():
    global a
    a = 4  # local variable
    var = 200
    print('fun1',id(var))
    print(f'in function1 = {var}')


def function2():
    b = 8
    print(f'in function2 = {a}')


function1()
function2()
print('outside of all a = ', a)
