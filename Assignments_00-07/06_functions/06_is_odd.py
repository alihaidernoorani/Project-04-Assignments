def is_even(num):
  if num % 2 == 0:
    return True
  else:
    return False

def main():
  for i in range(10,20):
    if is_even(i):
        print(i, "even")
    else:
        print(i, "odd")

if __name__ == "__main__":
    main()