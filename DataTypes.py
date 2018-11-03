# Defining Variables in Python.

name = "Rajashekhar Ramayampeta"
a = 10
b = 20
milesRanIn2017 = 1200

print(name)
print(a)
print(b)
print(milesRanIn2017)

# assign single value to multilple variables
x = y = z = 1

print(x, y, z)

x, y, z = 1, 2, 'Python'

print(x, y, z)

# Python Data types
# 1. Numbers, 2. String 3. List 4. Tuple 5. Dictionary


# Number

age = 1

# String

name = "Learn Daily"

# List

myList = ["a", 1, 1.3, "Python"]

print(myList)  # print whole list
print(myList[1])  # print 2nd element i.e 1
print(myList[1:3])  # print from 2nd to 3rd element in myList
print(myList*2)

myList2 = ['a', 2]

print(myList+myList2)  # concatenated lists

myTuple = ("a", 1, 1.3, "Python")

print(myList)  # print whole myTuple
print(myList[1])  # print 2nd element i.e 1
print(myList[1:3])  # print from 2nd to 3rd element in myList
print(myList*2)

myTuple2 = ('a', 2)

print(myTuple+myTuple2)  # concatenated tuples

# tuples read only , cannot be updated but list can be updated
myList[0] = "Raja Ramayampeta"

print(myList)

myTuple[0] = 'Raja Ramayampeta'  # error
print(myTuple)

# Dictionary : Key value pairs

dict = {}
dict['name'] = 'Raja'
dict[2] = 28

print(dict)

personDictionary = {'name': 'Rajashekhar','age': 28, 'profession': 'Software Developer'}

print(personDictionary['name'])
print(personDictionary.keys())
print(personDictionary.values())










