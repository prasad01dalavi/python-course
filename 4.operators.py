a, b = 2, 1 
c = 2

if a == c and b == 1:
    print('yes')

# and => when both conditions need to be satisfied
# or => if one of the condition is need to be satisfied
# not => performs opposite operation e.g. not(True) = False
if b != c:
    print('b is not c')

print(f'b!=c = {b!=c}')
print(f'not(True) = {not(True)}')
if not(b!=c):
    print('this is true')
else:
    print('this is not true')

# is and in
# in is used to find whether the element is present in "iterable" or not
a = [1, 2, 3, 4]

if 2 in a:
    print('yes 2 in a')

s = 'hello world'

if 'hell' in s:
    print('yes hell is present in s')

b = [1, 2, 3, 4]

if a == b:
    print('a == b is correct')

c = a
print('mem of a:', id(a))
print('mem of b:', id(b))
print('mem of c:', id(c))

if a is c:
    print('a is b is also correct') 

# == just check for contents and not main object (memory location can be different)
# is check for both contents and main object (memory location must be same)
