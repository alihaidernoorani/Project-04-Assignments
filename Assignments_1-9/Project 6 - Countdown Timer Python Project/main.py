import time

def countdown_timer(timer):
    while timer > 0:
        minutes, seconds = divmod(timer, 60)
        print(f"{minutes:02d}:{seconds:02d}", end="\r", flush=True)
        time.sleep(1)
        timer -= 1
    print("00:00")
    print("Time's up!")

if __name__ == "__main__":
    try:
        timer = int(input("Enter the time in seconds: "))
        countdown_timer(timer)
    except ValueError:
        print("Please enter a valid number.")
