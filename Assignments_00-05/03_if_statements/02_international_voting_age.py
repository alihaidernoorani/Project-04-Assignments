def main():
    age: int = int(input("How old are you? "))
    if age > 48:
      print("You can vote in Peturksbouipo where the voting age is 16. You can vote in Stanlau where the voting age is 25. You can vote in Mayengua where the voting age is 48.")
    elif age > 25:
      print("You can vote in Peturksbouipo where the voting age is 16. You can vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.")
    elif age > 16:
      print("You can vote in Peturksbouipo where the voting age is 16. You cannot vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.")
    else:
      print("You are too young to vote")

if __name__ == '__main__':
    main()