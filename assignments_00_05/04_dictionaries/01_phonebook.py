def add_contact(phonebook):
    name = input("Name: ")
    number = input("Number: ")
    if name in phonebook:
        print(f"{name} already exists in the phonebook")
    else:
        phonebook[name] = number
        print(f"{name} added successfully.")

def search_contact(phonebook):
    name = input("Enter name to search: ")
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        print(f"{name} is not in the phonebook")

def delete_contact(phonebook):
    name = input("Enter name to delete: ")
    if name in phonebook:
        del phonebook[name]
        print(f"{name} deleted successfully.")
    else:
        print(f"{name} is not in the phonebook")

def print_phonebook(phonebook):
    if phonebook:
        print("Contact list:")
        for name, number in phonebook.items():
            print(f"{name}: {number}")
    else:
        print("Phonebook is empty")

def main():
    phonebook = {}

    while True:
        print("\nPhonebook Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Show All Contacts")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_contact(phonebook)
        elif choice == '2':
            search_contact(phonebook)
        elif choice == '3':
            delete_contact(phonebook)
        elif choice == '4':
            print_phonebook(phonebook)
        elif choice == '5':
            print("Exiting Phonebook. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
