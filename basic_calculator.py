# while loop when you don't know how many time loop runs
# for loop when you know how many time loop runs

def addition(x, y):
    return x + y


def subtraction(x, y):
    return(x - y)


def multiplycation(x, y):
    return(x * y)


def divition(x, y):
    return(x // y)

# if only depends on condition
# elif depends on both if and right
# else depends only on if stememnts


run = True
while(run):
    print("1. add two numbers\n2. Subtract two numbers\n3. Multiply two numbers\n4. Divide two numbers\n5. Exit")

    x = int(input("Choose one of them: "))
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))

    if x == 1:
        print("result is ")
        print(addition(num1, num2))
    if x == 2:
        print("result is ")
        print(subtraction(num1, num2))
    if x == 3:
        print("result is ")
        print(multiplycation(num1, num2))
    if x == 4:
        print("result is ")
        print(divition(num1, num2))
    if x == 5:
        run = False
