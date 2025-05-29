import random

winning_cases = {
    'r': 's',  # Rock beats Scissors
    'p': 'r',  # Paper beats Rock
    's': 'p'   # Scissors beats Paper
}

def rock_paper_scissors_game():
    user = input("Choose 'r' for Rock, 'p' for Paper, or 's' for Scissors: ").lower()
    computer = random.choice(['r', 'p', 's'])

    if user not in winning_cases:
        print("❌ Invalid choice! Please pick 'r', 'p', or 's'.")
        return

    names = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    print(f"\nYou chose {names[user]}, Computer chose {names[computer]}.")

    if user == computer:
        print("🤝 It's a tie!")
    elif winning_cases[user] == computer:
        print("🎉 You win!")
    else:
        print("💻 Computer wins!")

if __name__ == "__main__":
    rock_paper_scissors_game()
