def double(num):
  double_num = num * 2
  print("Double that is",double_num)

def main():
  num: int = int(input("Enter a number: "))
  double(num)

if __name__ == "__main__":
  main()