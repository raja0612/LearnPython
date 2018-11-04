
# for loops

basket = ['apple', 'banana', 'peach']

for fruit in basket:
    print(fruit)

for letter in 'PYTHON':
    print(letter)

print('\n', 'break')
for fruit in basket:
    if fruit == 'banana':
        print('break when fruit is Banana and you won''t see other fruits in basket')
        break
    print(fruit)
print('\n', 'continue')
for fruit in basket:
    if fruit == 'banana':
        print('skip only when fruit is banana but you will see other fruits in basket')
        continue
    print(fruit)


# Python Loops

i = 1
while i <= 10:
    print('i', i)
    i += 1

j = 1
while j <= 5:
    if j == 3:
        print('Break loop when j is 3', j)
        break
    print('j', j)
    j += 1


embrace = ['diversity', 'freedom', 'racism', 'kindness']

x = 0
while x < 4:
    if embrace[x] == 'racism':
        continue
    print('embrace', embrace[x])
    x += 1
print('Fight for what is right')











