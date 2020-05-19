# when there is only one condition to check, then only if is fine
# when there are only two condition then, we will use if and else (e.g. even or odd)
# If all if conditions(if+elif) fails, it executes the else
# If first if condition fails it execute subsequent elif and exit

num = 11 

if num == 10:
    print('In if condition, number is 10')
elif num == 11:
    print('In elif condition number is 11')
elif num == 12:
    print('In elif condition number is 12')
else:
    print('In else condition, expected number is not present')

print('------')
if num == 10:
    print('num is 10')
if num == 11:
    print('num is 11')
if num == 12:
    print('num is 12')

if num == 20:
    pass
