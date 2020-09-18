# Displays the menu
# Returns the option chosen
def getOption():
    print("Options:" "1:Add\n" "2:Subtract\n" "3:Multiply\n" "4:Divide\n" "5:Quit")
    option = int(input("Enter an option: "))
    return option


# Returns the values to operate on
def getValues():
    value1 = float(input("Enter the first value: "))
    value2 = float(input("Enter the second value: "))
    return value1, value2


# main calculator loop
run = True
while run:
    opt = getOption()

    # terminate early if quitting
    if opt == 5:
        print("Terminating program")
        run = False
    else:

        # only get values
        # if necessary
        v1, v2 = getValues()

        # operators ordered on menu
        if opt == 1:
            print(v1 + v2)
        elif opt == 2:
            print(v1 - v2)
        elif opt == 3:
            print(v1 * v2)
        elif opt == 4:
            print(v1 / v2)
        else:
            # crude error handling
            print("Invalid Option")
