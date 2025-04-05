num_list = []
num_count_dict = {}

def count_number(number):
  num_count_dict[number] = num_count_dict.get(number, 0) + 1

def main():
  while True:
    number = input("Enter a number: ")
    if number == "":
      print("\n")
      break
    number = int(number)
    num_list.append(number)
    count_number(number)

  for key, value in num_count_dict.items():
    print(f"{key} appears {value} times")

if __name__ == '__main__':
    main()