# if types are the nouns of programming
# then functions are the verbs
# functions are an "identifier" followed by parenthesis
# some with "arguments" the function needs to work
# some without any
# some function return a value
# others don't

print("Hello World")  # prints string argument to the console
# doesn't return any value.

x_in = input()  # returns string input from the console
# doesn't expect any arguments

# There are a very large number of built-in functions in python
# all of the operators we have been using up this point are
# special types of functions with unique syntax (e.g. '=')
x = 2
x += 1
x -= 0

# Python libariers and modules are sets of functions other
# developers have made to expand the built-in capabilites of
# Python or to make it easier to use

# A Developer can write their own function using the "def"
# keyword, along with a unique identifier, and a code block
# definition
def example_func1(arg1, arg2):
    return arg1 + arg2
    # this function returns an addition and take two args


def example_func2():
    print("Hello Learners")
    # this function takes no arguments and returns nothing


example_func1()
example_func2()


# Functions are a useful way to prevent repeating code
# there is a principle of software developers referred to as 'DRY'
# DON'T REPEAT YOURSELF
# To make your code easier to understand, maintain, and debug
# Keep duplicate code to a minimum
# Putting useful bits of code into a function allows that code to be used
# repeatedly, while only being defined in one place
