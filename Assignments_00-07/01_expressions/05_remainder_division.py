def main():
    num1: int = int(input("Please enter an integer to be divided: "))
    num2: int = int(input("Please enter an integer to divide by: "))
    quotient: int = num1 // num2 # Divide with no remainder/decimals (integer division)
    remainder: int = num1 % num2 # Get the remainder of the division
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

if __name__ == '__main__':
    main()