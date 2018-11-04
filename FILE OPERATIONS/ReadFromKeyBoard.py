
# raw_input('Enter your input:')  # If you use Python 2
name = input('Enter your name:')      # If you use Python 3

print('You entered', name)

f = open("demofile.txt", "r")
print(f.read())

# Return the 5 first characters of the file:

f = open("demofile.txt", "r")
print(f.read(5))

# Read one line of the file:

f = open("demofile.txt", "r")
print(f.readline())

# Loop through the file line by line:

f = open("demofile.txt", "r")
for x in f:
  print(x)

# Open the file "demofile.txt" and append content to the file:

f = open("demofile.txt", "a")
f.write("Now the file has one more line!")

# Open the file "demofile.txt" and overwrite the content:

f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")
