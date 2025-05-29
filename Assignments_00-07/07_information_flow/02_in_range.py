def in_range(n, low, high):
    if low <= n <= high:
        return True
    return False

def main():
    while True:
      try:
          n = int(input("Enter a number to check: "))
          low = int(input("Enter the lower bound: "))
          high = int(input("Enter the upper bound: "))

          if in_range(n, low, high):
              print(f"{n} is within the range [{low}, {high}].")
          else:
              print(f"{n} is NOT within the range [{low}, {high}].")

          break
      except ValueError:
          print("Please enter valid integers for all inputs.")

if __name__ == "__main__":
    main()
