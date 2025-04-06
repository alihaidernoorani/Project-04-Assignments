import random

words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
       coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
       lion lizard llama mole monkey moose mouse mule newt otter owl panda
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
       skunk sloth snake spider stork swan tiger toad trout turkey turtle
       weasel whale wolf wombat zebra'''.split()

def hangman_game():
  word = random.choice(words)

  letters = list(word)
  current_word = ['_' for _ in letters]
  guessed_letters = set()
  lives = 6

  # Loop while the word is incomplete and player has lives remaining
  while '_' in current_word and lives != 0:
    guessed_letter = input("Guess a letter: ").lower()

    # Check if the input is a valid single letter
    if not guessed_letter.isalpha() or len(guessed_letter) != 1:
      print("Please enter a single letter (a-z).")
      continue

    # If the letter has not been guessed before
    if guessed_letter not in guessed_letters:
      guessed_letters.add(guessed_letter)
      if guessed_letter not in letters:
        print(f"Your guessed letter {guessed_letter} is not in word")
        lives -= 1 # Deducts a life if guess is incorrect

      print(f"You have {lives} left and have used these letters: {', '.join(sorted(guessed_letters))}")

      for i in range(len(letters)):
          if letters[i] == guessed_letter:
            current_word[i] = guessed_letter
      print(' '.join(current_word))
      print()

    # If the letter has already been guessed, print a message
    else:
      print("You have already used that character\n")

  if '_' in current_word:
    print("💀 You lost! The word was:", word)
  else:
    print("🎉 You won! The word was:", word)

if __name__ == "__main__":
    hangman_game()


