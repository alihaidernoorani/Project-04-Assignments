ADULT_AGE: int = 18

def is_adult(age):
  if age > ADULT_AGE:
    return True

  return False

def main():
  while True:
    try:
      age: int = int(input("How old is this person?: "))
      print(is_adult(age))
      break
    except ValueError:
      print("Enter a valid integer!")

if __name__ == "__main__":
    main()