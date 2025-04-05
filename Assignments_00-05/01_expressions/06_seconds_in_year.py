# Constants
days_in_a_year: int = 365
hours_in_a_day: int = 24
minutes_in_an_hour: int = 60
second_in_a_minute: int = 60

def main():
    seconds_in_a_year: int = days_in_a_year * hours_in_a_day * minutes_in_an_hour * second_in_a_minute
    print(f"There are {seconds_in_a_year} seconds in a year")

if __name__ == '__main__':
    main()