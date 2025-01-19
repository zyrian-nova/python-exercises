# Write a program that calculates the average of three test scores and assigns a grade based on the result.
# Requirements:
# Ask the user for three test scores (numbers).
# Calculate the average of the scores.
# Assign a grade based on the average:
# A for 90 and above.
# B for 80-89.
# C for 70-79.
# D for 60-69.
# F for below 60.
print("Enter three test scores in numeric value.")
score1 = float(input("Score one: "))
score2 = float(input("Score two: "))
score3 = float(input("Score three: "))
average = (score1 + score2 + score3) / 3
print(f"Average score: {average}") # f"{average:.2f}" limits the average to two decimal places for better readability.
if average >= 90:
    print(f"Grade: A")
elif average >= 80:
    print(f"Grade: B")
elif average >= 70:
    print(f"Grade: C")
elif average >=60:
    print(f"Grade: D")
else:
    print(f"Grade: F")