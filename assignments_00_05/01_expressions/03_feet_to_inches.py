def main():
    feet: float = float(input("Enter the number of feet: "))
    inches: float = feet*12
    print(f"That is equal to {inches:.2f} inches")

if __name__ == '__main__':
    main()