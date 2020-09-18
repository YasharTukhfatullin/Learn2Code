# Create a phone book that users can enter names
# and numbers into and then print out all of the contents.

user_name = {}
user_phone = {}


def create():
	user_name = input("Enter user name:")
	user_phone = int(input("Enter the number"))
	user_name[user_phone] = {"name": user_name, "phone": user_phone}


while create():
	pass
