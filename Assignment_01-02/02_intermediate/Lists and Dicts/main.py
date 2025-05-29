# Problem #1: List Practice

def main():
    fruit_list: list[str] = ["apple", "banana", "orange", "grape", "pineapple"]

    # Print the length of the list
    print(f"The length of the list: {len(fruit_list)}")

    # Add 'mango' at the end of the list. 
    fruit_list.append("mango")

    # Print the updated list.
    print(f"Updated list: {fruit_list}")

if __name__ == "__main__":
    main()

# Problem #2: Index Game

def access_element(lst, index):
    if 0 <= index < len(lst):
        return f"Element at index {index} is: {lst[index]}"
    else:
        return "Index out of range."

def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        old_value = lst[index]
        lst[index] = new_value
        return f"Replaced '{old_value}' with '{new_value}' at index {index}."
    else:
        return "Index out of range."

def slice_list(lst, start, end):
    if start < 0 or end > len(lst) or start > end:
        return "Invalid start or end indices."
    return lst[start:end]

def print_menu():
    print("\nChoose an operation:")
    print("1. Access an element")
    print("2. Modify an element")
    print("3. Slice the list")
    print("4. Show current list")
    print("5. Exit")

def index_game():
    my_list = ["apple", "banana", "cherry", "date", "elderberry"]

    print("Welcome to the Index Game! 🎮")
    print(f"Here's your starting list: {my_list}")

    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            try:
                index = int(input("Enter the index to access: "))
                print(access_element(my_list, index))
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == "2":
            try:
                index = int(input("Enter the index to modify: "))
                new_value = input("Enter the new value: ")
                print(modify_element(my_list, index, new_value))
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == "3":
            try:
                start = int(input("Enter the start index: "))
                end = int(input("Enter the end index: "))
                result = slice_list(my_list, start, end)
                print(f"Sliced list: {result}")
            except ValueError:
                print("Please enter valid numbers.")
        
        elif choice == "4":
            print(f"Current list: {my_list}")
        
        elif choice == "5":
            print("Thanks for playing the Index Game! 👋")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    index_game()
