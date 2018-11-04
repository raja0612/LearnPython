# Python functions

# function declaration


def print_name (name):
    "This prints a passed string into this function # optional docstring"
    print('Your name is ', name)
    return


# function calling
print_name('Python')


def assign_default_param(nation = 'mars'):
    return print('I''m from', nation)


assign_default_param('USA')
assign_default_param()

# lamdas are anonymous function which can take any number of arguments but only one expression

x = lambda a: a + 10
print(x(5))
print(lambda a: a + 10)


def my_lambda(n):
    return lambda a: a * n  # returns anonymous function


print(my_lambda(2)(5))













