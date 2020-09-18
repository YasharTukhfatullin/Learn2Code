# So far we've only worked with one value at a time
# but quite often we'd like to work with many values at once
# python provides a few basic types of containers to work with mutiple values
# the most common and basic of which, is a list
example_list = [
    1,
    "two",
    3.0,
    True,
]  # lists can store multiple values of different types
example_list.append("Hello")
print(example_list)


maintainable_list = [
    1,
    2,
    3,
    4,
]  # unless absolutely necessary, its usually best practice to keep types uniform

# lists (as a python class) have a handful of built-in functions
# we use these functions using object dot notations ("." operator)
empty_list = []
empty_list.append(1)
empty_list.insert(0, 2)
empty_list.sort()
empty_list.reverse()
x = empty_list[1]  # returns the value at index 1

# dictionaries are another type of container
# but instead of indexing into the container using a integer
# we access values using keys
# example_dict = {"key": "value", 1: "blue", True: 3}
# print(example_dict)


# lists and dictionaries (and other containers) can be "nested"
# allowing for mulit-dimensional data to be represented
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

dict_of_dicts = {
    "dict_this": {"value1": "red", "value2": "blue"},
    "dict_that": {"value1": True, "value2": False},
}
print(list_of_lists)
print(dict_of_dicts)
print(dir(list_of_lists))

# More containers to come...


def returns_multiple_func():
    return 1, 2, 3


x, y, z = returns_multiple_func()
x + y + z

