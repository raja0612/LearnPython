class Person:
    # properties
    name = 'Rajashekhar Ramayampeta'

# just like constructor
    def __init__(self):
        self.language = 'Python'
        self.pet = 'Max'
        self.interests = ['coding', 'running', 'sana bina']

# methods
    def hobbies(self):

        for interest in self.interests:
            print(interest)


# object creation


person = Person();

print(person.name)

print(person.language)
print(person.pet)


person.hobbies()

