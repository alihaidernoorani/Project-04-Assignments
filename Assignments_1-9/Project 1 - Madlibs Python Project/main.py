def madlib_game():
    adj = input("Enter an adjective: ")
    verb1 = input("Enter a verb: ")
    verb2 = input("Enter another verb: ")
    noun = input("Enter a noun: ")

    madlib = f"Computer programming is so {adj}! I love to {verb1} and {verb2} while working on {noun}. It makes me feel like a genius!"

    print("\nHere's your Mad Lib story:")
    print(madlib)

if __name__ == "__main__":
    madlib_game()

