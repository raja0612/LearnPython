#! \usr\bin\pyhton

import numpy as np
import matplotlib.pyplot as plt


# read Salaries.txt using np library
salaries = np.fromfile("Salaries.txt", dtype=int, sep=",")

print(salaries)

names = np.genfromtxt("Names.txt", dtype='str', delimiter=",")

print(names)


# create graph x axis values

x = np.arange(len(names))

print(x)

plt.bar(x, salaries)

plt.xticks(x, names)
plt.ylabel("Salaries")
plt.xlabel("Names")
title = 'Salary of ', len(names),'random people'
plt.title(title)
plt.show()
