# Python - Operators


# Arithmetic Operators
a = 2
b = 2

c = a+b
print("addition", c)

c = a-b
print("subtraction", c)

c = a*b
print("multiplication", c)

c = a/b
print("division", c)
print(c)

c = a % b
print("modulus", c)

c = a//b
print("Floor Division", c)


c = a**b
print("Exponent", c)

# comparision operators

print("Equals", a == b)

print("not equals", a != b)

print("Greater Than", a > b)

print("Less than", a < b)

print("Greater Than or Equal",a >= b)

print("Less Than or Equal", a <= b)

# bit wise operators .performs on bits

a = 15
b = 16

print("Binary AND", a & b)
print("Binary OR", a & b)
print("Binary NEGATION", ~a)
print("Binary LEFT SHIFT", a << b)
print("Binary RIGHT SHIFT", a >> b)

# Membership Operators

a = [1, 2, 'Python']

print('in operator', 1 in a)

print('not in operator', 'Python' not in a)

# identity operators, checks the address of objects

x = y = 1

print('is operator', x is y)

print('is not operator', x is not y)







