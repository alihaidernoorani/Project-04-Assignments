import random

def roll_dice():
  die1: int = random.randint(1,6)
  die2: int = random.randint(1,6)
  total: int = die1 + die2
  print(f"Die 1: {die1}, Die 2: {die2} → Total: {total}")

def main():
   for _ in range(3):
      roll_dice()

if __name__ == '__main__':
    main()