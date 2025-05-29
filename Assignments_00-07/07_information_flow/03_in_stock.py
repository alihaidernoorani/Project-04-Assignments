def num_in_stock(fruit):
	if fruit == 'apple':
		return 2
	elif fruit == 'durian':
		return 4
	elif fruit == 'pear':
		return 1000
	else:
		# this fruit is not in stock.
		return 0

def main():
  fruit: str = input("Enter a fruit: ")
  stock: int = num_in_stock(fruit)
  if stock != 0:
    print(f"The fruit is in stock! Here is how many: {stock}")
  else:
    print("The fruit is not in stock.")

if __name__ == "__main__":
    main()
