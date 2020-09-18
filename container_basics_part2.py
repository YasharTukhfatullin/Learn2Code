# Variables are good for storing a single value
car_title = "Pontiac G6"
car_title = "Ford Focus"  # We lose the previous

# Python lists are used for storing multiple values
# Python lists are different from other languages,
# in that they can store different types
list_example = [1, "String", True]  # Usually better to be avoided in favor of a class
list_example.append(5)
print(list_example)

# Operate key/value pairs
dict_example = {
    "Horse": {"Name": "Ryan", "Experience": "Master Level"},  # Curly brackets to define
    "Mogul": "Yash",
    "Wizard": "Bryson",
    "Soyboy": "Jake",
}

print(dict_example["Horse"])  # Use square brackets to access key/value pairs

# Lists: Order can be important (represent concepts where order matters)
# Dictionaries: Heirarchy is important (*ditto*)
# Lists: represent sets
# Dictionaries: represent maps
# Tuples: represent ordinals

# Set is just a collection of different things [3,1,7,9,51...] == [1,3,5,7,9...]
# Ordinal is a collection, where order is meaningful (1,2,3) != (2,3,1)
# Map is a relationship between sets [a,b,c] --> [1,2,3] == { a : 1, b : 2, c : 3}


def returns_multiple_func():
    return 1, 2, 3


x, y, z = returns_multiple_func()
x + y + z

# Empty tuple
empty_tuple = ()
# Create an initialized tuple
example_tuple = (0, 0, 0)
# Store all three into single variable
example_tuple = returns_multiple_func()
print(example_tuple)
