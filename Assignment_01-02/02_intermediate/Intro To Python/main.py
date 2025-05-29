gravitational_constants = {
    "Mercury": 37.6,
    "Venus": 88.9,
    "Mars": 37.8,
    "Jupiter": 236.0,
    "Saturn": 108.1,
    "Uranus": 85.1,
    "Neptune": 114.0
    }

def main():
   earth_weight: float = float(input("Enter a weight on Earth: "))
   planet: str = input("Enter a planet: ")
   mars_weight: float = gravitational_constants[planet] * earth_weight / 100
   rounded_mars_weight: float = round(mars_weight, 2)
   print(f"The equivalent weight on {planet}: {rounded_mars_weight}")

if __name__ == "__main__":
    main()