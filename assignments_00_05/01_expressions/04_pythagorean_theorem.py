import math

def main():
    length_of_side_AB: float = float(input("Enter the length of AB: "))
    length_of_side_AC: float = float(input("Enter the length of AC: "))
    length_of_hypotenuse_BC: float = math.sqrt(length_of_side_AB**2 + length_of_side_AC**2)
    print(f"The length of BC (the hypotenuse) is: {length_of_hypotenuse_BC}")

if __name__ == '__main__':
    main()