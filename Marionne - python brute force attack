#Exercise 6: Brute Force Attack
#Marionne Jizella E. Centeno
import itertools
import string
import time

# Target password (for demo)
target_password = "ab3"

# Characters that can be used
characters = string.ascii_lowercase + string.digits

attempts = 0
start_time = time.time()

print("Starting brute force simulation...\n")

# Try every combination
for length in range(1, 6):  # max password length
    for guess in itertools.product(characters, repeat=length):
        attempts += 1
        guess_password = ''.join(guess)

        print(f"Attempt {attempts}: {guess_password}")

        if guess_password == target_password:
            end_time = time.time()
            print("\nPassword Found!")
            print("Password:", guess_password)
            print("Attempts:", attempts)
            print("Time taken:", round(end_time - start_time, 2), "seconds")
            exit()
