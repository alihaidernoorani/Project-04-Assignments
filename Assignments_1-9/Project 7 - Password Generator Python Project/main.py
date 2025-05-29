import random
import string

def generate_passwords(number, length):
    characters = string.ascii_letters + string.digits + '@/!#'
    for _ in range(number):
        password = ''.join(random.choices(characters, k=length))
        print(password)

def main():
    while True:
        try:
            number = int(input("Please enter the number of passwords to generate: "))
            length = int(input("Please enter the length of each password: "))
            generate_passwords(number, length)
            break
        except ValueError:
            print("Please enter a valid integer.")
            continue

if __name__ == "__main__":
    main()
