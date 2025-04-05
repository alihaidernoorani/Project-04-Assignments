import random

def main():
    secret_number = random.randint(1, 99)
    print("I am thinking of a number between 1 and 99...")

    while True:
        try:
            guess = int(input("Enter a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < secret_number:
            print("Your guess is too low\n")
        elif guess > secret_number:
            print("Your guess is too high\n")
        else:
            print("Congrats! The number was:", secret_number)
            break

if __name__ == '__main__':
    main()
