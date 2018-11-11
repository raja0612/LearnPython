f = open('birds.txt', 'r')

data = f.read()

# split the words with space.
words = data.split(" ")

# no of lines.
lines = data.split('\n')

print("\n *********************WORDS***************** \n")
for word in words:
    print(word)

# len() is python inbuilt function to find the length of List
print('Number of words in this file are', len(words))

print("\n *********************LINES***************** \n")

i = 0
for line in lines:
    if len(line) != 0:
        i += 1
        print(line)


print('Wrong Number of Lines in this file', len(lines))
print('Correct Number of Lines in this file', i)
print('No of empty lines are', len(lines)-i)
