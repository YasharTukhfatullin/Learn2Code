# What can you do with primitives and variables?
# Not much on their own, but a lot with a little bit of
# control statements
# the most common (and relatively powerful) control flow statement
# is the if () statement
condition = False
if condition:
    # an if statement depends on the "evaluation" of a boolean condition
    # ONLY if the condition evaluates to True does the code inside of
    # the if "block" get run
    x = 1
    condition = True
elif condition:
    # an elif statement depends on the evaluation of a boolean as well
    # as the evaluation of the most recent if statement (and therefore its condition)
    x = 2
    condition = False
else:
    # an else statement only depends on the evalutation of the previous
    # if statement (and therefore its condition)
    x = 3
    condition = True

# Another type of control statement are loops
# A for loop is used to repeat a code block a known number of times
for i in range(0, 100):
    # The code inside of here will repeat 100 times
    x = x + 1

# While loops are used to repeat a code block an unkown number of times
# until a certain condition is met
while x <= 200:
    # the code inside this block will run until x > 200
    x /= 2
    x + 100
