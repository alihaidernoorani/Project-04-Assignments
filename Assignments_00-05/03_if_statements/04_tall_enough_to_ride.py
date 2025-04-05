minimum_height: float = 50

def tall_enough_extension(height):
  if height >= minimum_height:
    print("You're tall enough to ride!")
  else:
    print("You're not tall enought to ride, but maybe next year!")

def main():
    try:
      while True:
        user_input = input("How tall are you? ")
        if user_input.strip() == "":
          break
        height = float(user_input)
        tall_enough_extension(height)
    except ValueError:
      print("Please enter a valid height")

if __name__ == '__main__':
    main()