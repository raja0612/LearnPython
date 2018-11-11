import numpy as np

x = [5, 10, 15, 20, 25]

y = []

for value in x:
    y.append(value / 5)

print("\nOld fashioned way: x = {} y = {} \n".format(x, y))

# list comprehensions;

# syntax [do something for list]

z = [value / 5 for value in x]

print("List Comprehensions: x = {} z = {} \n".format(x, z))


try:
    a = x / 5
except:
    print('You cannot do with Python Lists \n')
    a = np.array(5)
    print('using np library converted list to array so we can divide each array value by 5', a)
    b = a / 5


print("Using numpy: a = {} b = {} \n".format(a, b))


