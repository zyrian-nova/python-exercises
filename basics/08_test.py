"""
Create a number guessing game where the user has to guess a randomly generated number.
Requirements:
Generate a random number between 1 and 100.
Let the user guess the number.
Use a loop to allow multiple attempts, providing feedback:
"Too high" if the guess is greater than the number.
"Too low" if the guess is less than the number.
End the game when the user guesses correctly and display the number of attempts.
"""
import random

increment = 1
rng = random.randint(1,100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

while True:
    try:
        usernum = int(input("Guess the number I'm thinking!: "))
        if usernum < 1 or usernum > 100:
            print("Please enter a number between 1 and 100!")
            continue

        if usernum > rng:
            print("Too high!")
        elif usernum < rng:
            print("Too low")
        else:
            print(f"Congratulations! You gessed the number in {increment} tries, you're a wizard Harry! 🧙‍")
            break
        increment += 1
    except ValueError:
        print("Invalid input. Please enter a valid number.")
