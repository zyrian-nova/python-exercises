# Create a number guessing game where the user has to guess a randomly generated number.

# Requirements:

# Generate a random number between 1 and 100.
# Let the user guess the number.
# Use a loop to allow multiple attempts, providing feedback:
# "Too high" if the guess is greater than the number.
# "Too low" if the guess is less than the number.
# End the game when the user guesses correctly and display the number of attempts.
import random

counter = 0
rng = random.randint(1,100)
print(rng)

usernum = int(input("Guess the number I'm thinking!: "))
if usernum == rng:
    print("You gessed the number, you're a wizard Harry!")
elif usernum >= rng:
    print("Too high")
else:
    print("Too low")
counter +=1