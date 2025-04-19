def print_multiple(message,repeats):
  for _ in range(repeats):
    print(message)

def main():
  while True:
    try:
      message: str = input("Please type a message: ")
      repeats: int = int(input("Enter number of times to your message: "))
      print_multiple(message, repeats)
      break

    except ValueError:
      print("Enter a valid integer in repeats")

if __name__ == "__main__":
    main()