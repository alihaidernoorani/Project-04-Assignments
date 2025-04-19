import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    round: int = 1
    score: int = 0

    while round <= NUM_ROUNDS:
        computer_number: int = random.randint(1, 100)
        user_number: int = random.randint(1, 100)

        print(f"Round {round}")
        print(f"Your number is {user_number}")

        user_input: str = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()

        # Keep asking until valid input is given
        while user_input not in ["higher", "lower"]:
            user_input = input("Please enter either 'higher' or 'lower': ").strip().lower()

        if user_number > computer_number and user_input == "higher":
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        elif user_number < computer_number and user_input == "lower":
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        elif user_number == computer_number:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")

        print(f"Your score is now {score}\n")
        round += 1

    print(f"Your final score is {score}/{NUM_ROUNDS}")
    
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score > NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
