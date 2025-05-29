# Constant value for the speed of ligh
c: int = 299792458

def main():
    mass: float = float(input("Enter kilos of mass: "))
    energy: float = mass*c**2
    print("e = m * C^2...")
    print(f"m = {mass} kg")
    print(f"C = {c} m/s")
    print(f"{energy} joules of energy")

if __name__ == '__main__':
    main()