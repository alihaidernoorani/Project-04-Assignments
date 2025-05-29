import random

def user_guess(max_number):
  secret_number = random.randint(1, max_number)
  guess = 0

  while guess != secret_number:
    try:
      guess = int(input(f"Guess the secret number between 1 and {max_number}: "))
      if guess > secret_number:
        print("Sorry, guess again. Your guess is too high")
        print()
      elif guess < secret_number:
        print("Sorry, guess again. Your guess is too low")
        print()
    except ValueError:
      print(f"Invalid input! Enter a valid integer between 1 and {max_number}")

  print(f"Congratulations! You guessed the number {secret_number} correctly ")

if __name__ == "__main__":
    user_guess(10)
