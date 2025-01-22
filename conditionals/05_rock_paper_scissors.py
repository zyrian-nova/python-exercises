"""
Create a simple Rock, Paper, Scissors game:
Ask the user to input their choice (rock, paper, or scissors).
Randomly generate the computer's choice.
Determine the winner using the following rules:
Rock beats scissors.
Scissors beat paper.
Paper beats rock.
If both choose the same, it's a tie.
Example Output:

Your choice (rock/paper/scissors): rock
Computer's choice: scissors
You win!
"""
import random
rng = random.randint(1,3)

try:
    user_choice = input("Your choice (rock/paper/scissors): ")
    TEXT = str.lower(user_choice)
    if TEXT not in {"rock", "paper", "scissors"}:
        print("Invalid choice. Please enter a valid selection.")
        exit()
except ValueError:
    print("Invalid input. Please enter a valid selection.")
    exit()

if rng == 1:
    PC_CHOICE = "rock"
elif rng == 2:
    PC_CHOICE = "paper"
else:
    PC_CHOICE = "scissors"
print(f"Computer's choice: {PC_CHOICE}")

# Logic block
if user_choice == "rock" and PC_CHOICE == "scissors":
    print("You win!")
elif user_choice == "paper" and PC_CHOICE == "rock":
    print("You win!")
elif user_choice == "scissors" and PC_CHOICE == "paper":
    print("You win!")
elif user_choice == PC_CHOICE:
    print("It's a draw!")
else:
    print("You lose!")


# A dictionary can be used to map winning conditions
# winning_conditions = {
#     "rock": "scissors",
#     "paper": "rock",
#     "scissors": "paper"
# }

# Then it can be determined using
# if PC_CHOICE == TEXT:
#     print("It's a draw!")
# elif winning_conditions[TEXT] == PC_CHOICE:
#     print("You win!")
# else:
#     print("You lose!")
