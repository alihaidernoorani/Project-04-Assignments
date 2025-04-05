import random

def main():
    die1: int = random.randint(1,6)
    die2: int = random.randint(1,6)
    total: int = die1 + die2
    print(f"First Die: {die1}")
    print(f"Second Die: {die2}")
    print(f"The total of the two dice: {total}")

if __name__ == '__main__':
    main()