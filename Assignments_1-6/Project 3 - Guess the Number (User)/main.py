import random

def computer_guess(max_value):
    low = 1
    high = max_value
    feedback = ''

    print(f"Think of a number between {low} and {high} and let the computer guess it!")

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # or high, since they're equal
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()

        if feedback == 'h':

            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback != 'c':
            print("Invalid input! Enter (H) for too high, (L) for too low or (C) for correct")

    print(f"Yay! The computer guessed your number {guess} correctly! 🎉")

if __name__ == "__main__":
    computer_guess(10)

