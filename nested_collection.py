# Collections themselves are value types
# (this makes some sense, a group of values could be a value)
# Since collections let you store values,
# You can store other collections inside of each other

# Example of three level dictionary
# Think Tree-like structure (remember heirarchical)
nested_dict = {
    "key1": 1,
    "key2": "string",
    "car": {"model": "kia", "color": "blue", "engine": {"cylinders": 6, "layout": "V"}},
}

# An example of the syntax for printing elements nested inside tree
# Each [] operator moves one more dictionary inward
print(nested_dict["car"]["engine"]["cylinders"])

# Nested lists are more focused on dimensionality
# Python nested lists can be jagged (but its better practice to be consistent)
# Syntax for use is pretty similar
nested_list = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]

# The prototypical example of 2D-Array is a tic tac toe board
tic_tac_toe_board = [["e", "e", "e"], ["e", "e", "e"], ["e", "e", "e"]]

# Helper functions for displaying and using the board
def print_board():
    print("----------")
    for row in tic_tac_toe_board:
        print(row)
    print("----------")


def player_move(x, y, p):
    tic_tac_toe_board[x][y] = p


# Typically, conditionals are done in the postive phrase
# winner = False
# while(not winner):


# Code shows how the indices work
# Depending on logic
# In this case the first one is the row
# And the second one is the column
print_board()
player_move(0, 0, "O")
print_board()
player_move(1, 1, "X")
print_board()
player_move(2, 2, "O")
print_board()


# You can mix and match collections as well!
ryan_info = {
    "name": "Ryan L Scott",
    "bday": "08/28/1996",
    "fave_fruits": ["apple", "grape", "orange", "lime", "lemon"],
}

ryan_info["fave_fruits"].append("cherries")
