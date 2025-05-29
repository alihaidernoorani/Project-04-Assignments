lst = []

def count_even(lst):
    count = 0
    for num in lst:
      if num % 2 == 0:
        count += 1
    return count

def input_lst():
      while True:
        num: int = input("Enter an integer or press enter to stop: ")
        if num == "":
          break
        try:
          lst.append(int(num))
        except ValueError:
          print("Enter valid integer")

def main():
  input_lst()
  print(count_even(lst))

if __name__ == "__main__":
    main()