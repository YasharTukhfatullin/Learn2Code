# Example of how you can use functions to separate menus
# and menu logic
# (Note that this can be broken apart even further)
# (MVC requires that you do break these down further!)

# The over arching menu (in a tree this is the root)
# Notice the parent calls the child
def main_menu():
    print("Press 1 for English")
    print("Press 2 for Spanish")
    print("Press 3 for Tartar")
    print("Press 4 to End")
    response = int(input("Enter Option: "))

    if response == 1:
        return english_menu()
    elif response == 2:
        print("Not yet implemented")
        return True
    elif response == 3:
        return tartar_menu()
    elif response == 4:
        return False
    else:
        print("Invalid Option")


# An example sub-menu
# Notice the child returns the value the parent needs
def english_menu():
    print("Press 1 to get sucked")
    print("Press 2 to get cucked")
    print("Press 3 to get fucked")
    response = int(input("Enter Option: "))

    if response == 1:
        return get_sucked()
    elif response == 2:
        return get_cucked()
    elif response == 3:
        return get_fucked()
    else:
        print("Invalid Option")
        return True


# More children/grandchildren below
# --------------------------------
def tartar_menu():
    print("Ask yash for 1")
    print("Ask yash for 2")
    print("Ask yash for 3")
    response = int(input("Enter Option: "))
    return True


def get_fucked():
    print("You got fucked")
    return True


def get_sucked():
    print("You got sucked")
    return True


def get_cucked():
    print("You got cucked")
    return True


while main_menu():
    print("----------")

