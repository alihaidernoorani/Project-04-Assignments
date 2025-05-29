import random

def done():
  return random.random() < 0.5

def chaotic_counting():
  for i in range(1,10):
    print(10-i)
    if done():
      return

def main():
  print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
  chaotic_counting()
  print("I'm done.")

if __name__ == "__main__":
    main()