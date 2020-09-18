phone_book = []

entry_example = {
    "name": "Ryan Scoot",
    "phone_number": "+15155122100",
    "type": "Residental",
}

phone_book.append(entry_example)


def create_entry():
    print("Create entry")
    name = input("Enter your name: ")
    phone = input("Enter Phone: ")
    t = input("Comerical or Residental")
    return {"name": name, "phone_number": phone, "type": t}


run = True
while run:
    print("1. Create an entry\n" "2. Print all name\n" "3. Print all number\n" "4. End")
    option = int(input())
    if option == 1:
        phone_book.append(create_entry())
    elif option == 2:
        for entry in phone_book:
            print(entry["name"])
    elif option == 3:
        for entry in phone_book:
            print("phone_number")
    elif option == 4:
        run = False
