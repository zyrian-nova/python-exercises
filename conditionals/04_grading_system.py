"""
Write a program that converts a numerical grade into a letter Letter grade:
A for 90 and above.
B for 80-89.
C for 70-79.
D for 60-69.
F for below 60.
Example Output:

Enter your Letter grade: 85
Letter Letter grade: B
"""
try:
    grade = int(input("Enter your grade: "))
    if grade < 0 or grade > 100:
        print("Invalid grade. Please enter a number between 0 and 100.")
        exit()
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

if grade >= 90:
    print("Letter grade: A")
elif grade >= 80:
    print("Letter grade: B")
elif grade >= 70:
    print("Letter grade: C")
elif grade >=60:
    print("Letter grade: D")
else:
    print("Letter grade: F")
