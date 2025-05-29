import random

def main():
    secret_number = random.randint(1, 99)

    print("Guess My Number")
    
    while True:
        try:
            guess = int(input("I am thinking of a number between 1 and 99... Enter a guess: "))
            break  # Exit loop if valid input is provided
        except ValueError:
            print("Please enter a valid number.")

    while guess != secret_number:
        if guess > secret_number:
            print("Your guess is too high")
        else:
            print("Your guess is too low")

        print()
        while True:
            try:
                guess = int(input("Enter a new number: "))
                break  # Exit loop if valid input is provided
            except ValueError:
                print("Please enter a valid number.")

    print(f"Congrats! The number was {secret_number}")

if __name__ == '__main__':
    main()
