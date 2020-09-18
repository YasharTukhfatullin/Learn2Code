# maybe something is wrong with
# the current state of program
def problematic_func():
    raise RuntimeError


class InputError(Exception):
    def __self__(self, expression, message):
        self.expression = expression
        self.message = message


def main_menu():
    try:
        option = int(
            input(
                "Enter an option:\t\n"
                "1. Display Options:\t\n"
                "2. Display Users:\t\n"
                "3. Exit:\t\n"
            )
        )
        if option == 1:
            pass
        elif option == 2:
            problematic_func()
        elif option == 3:
            return False
        else:
            raise InputError("main_menu()", "User input invalid option")

    except ValueError:
        print("Please enter a valid option :(")
    except RuntimeError:
        print("Something went wrong")
    # Something to fix the problem goes here
    except InputError:
        print("IDK WTF to print the message")
    else:  # only runs if no exceptions happenNo exceptions
        print("No exceptions happened")
    finally:  # this always runs regardless of exceptions
        print("I always run")
    return True


while main_menu():
    pass
