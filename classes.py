import random
from abc import ABC, abstractmethod 

# Classes are like blueprints for reusable memory structures
# Objects are like houses (or any other object you make from a blueprint)

# Definition
class Person:

    doTheySuck = True # Example of class variable

    def __init__(self, name, age, occupation, social_security): # constructor or initializer
        self.name = name # Example of an instance variable
        self.age = age
        self.occupation = occupation
        self._social_security = social_security # Theres no such thing as a private member variable
                                                # we pretend that theres privacy with _
    def getSocialSecurity(self): # Getter method tells developers this is what you meant to use
        return self._social_security

# Definition
def hello():
    print("Hello World")

# Somewhere in our code
# Function call
hello()

# Instantiate
person1 = Person("Ryan Scott", "23", "Backend Developer", 123456789)
person2 = Person("Jake S.", "27", "Not a CPA", 987654321)
person3 = Person("Yash T.", "27", "Student", 7894561234)

dumb_list = [person1, person2, person3]
Person.doTheySuck = False
for person in dumb_list:
    print("================")
    print(person.name)
    print(person.age)
    print(person.occupation)
    print(person._social_security)

person1._social_security = "Youre fucked bucko"

print(person1._social_security)

# name1 = "."
# age1 = "."
# occupation1 = "."

# name2 = "."
# age2 = "."
# occupation2 = "."

# name3 = "."
# age3 = "."
# occupation3 = "."

# return name, age, occupation
# name_1, age_1, occupation_1 = func_that_returns()

# Abstract class
class Animal(ABC):

    kingdom = "Animalia"

    def __init__(self, name, legs, eyes, fur):
        self.name = name
        self.legs = legs
        self.eyes = eyes
        self.fur = fur

    @abstractmethod
    def breathe(self):
        pass

# Instance Classes
class Monkey(Animal):

    def __init__(self, name):
        super(self, name, legs=2, eyes=2, fur=True)

    def breathe(self):
        print("Ook, ook")

class Pig(Animal):

    def __init__(self, name):
        super(self, legs=4, eyes=2, fur=False)

    def breathe(self):
        print("Breathe")

# For next lecture: Why would we do this?