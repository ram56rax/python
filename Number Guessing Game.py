import random

print ("Welcome to the Number Guessing Game!")
secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Guess a number between 1 and 100: ").strip()

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    guess = int(guess)
    attempts +=1

    if guess < secret_number:
        print("Too low! Try again.")

    elif guess > secret_number:
        print("Too high! Try again.")

    else:
        print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
        break            