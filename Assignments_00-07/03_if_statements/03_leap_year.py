def main():
   year: int = int(input("Enter the year. "))
   if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("That's a leap year!")
   else:
    print("That's not a leap year.")

if __name__ == '__main__':
    main()