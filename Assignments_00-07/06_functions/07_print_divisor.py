def print_divisors(num):
  for i in range(1,num + 1):
    if num % i == 0:
      print(i)

def main():
  while True:
    try:
      num: int = int(input("Enter a number: "))
      print_divisors(num)
      break
    except ValueError:
      print("Enter a valid integer")

if __name__ == "__main__":
    main()