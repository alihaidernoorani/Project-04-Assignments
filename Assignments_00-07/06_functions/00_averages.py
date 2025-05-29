def average(num1, num2):
  avg: int = (num1 + num2)/2
  return avg

def main():
  while True:
    try:
      num1: float = float(input("Enter first number: "))
      num2: float = float(input("Enter second number: "))
      print("Average:", average(num1, num2))
      print()
      continue_run = input("Want to continue (yes/no): ").lower()
      if continue_run != "yes" and continue_run != "y":
        break

    except ValueError:
      print("Please enter valid numbers")
      continue

if __name__ == "__main__":
    main()