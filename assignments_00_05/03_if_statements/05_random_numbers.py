import random

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
    num_list = []
    for i in range(N_NUMBERS):
      value = random.randint(MIN_VALUE, MAX_VALUE)
      num_list.append(value)
    print(*num_list) # Unpacks the list to print space-separated values

if __name__ == '__main__':
    main()