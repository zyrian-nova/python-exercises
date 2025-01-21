"""
Write a program that asks the user for two numbers and determines:
Which number is larger.
Whether the numbers are equal.
Example Output:

Enter the first number: 8
Enter the second number: 15
15 is larger than 8.
"""
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
except ValueError:
    print("Please enter valid numbers!")

if num1 == num2:
    print("Both numbers are equal!")
elif num1 > num2:
    print(f"{num1} is larger than {num2}.")
else:
    print(f"{num2} is larger than {num1}")
