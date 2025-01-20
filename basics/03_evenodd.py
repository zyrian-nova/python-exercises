"""
You will learn to use conditionals to determine if a number is even or odd.
Instructions:
Ask the user for a number.
Use a conditional structure to check if the number is divisible by 2.
"""
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"The number {num} it's even.")
else:
    print(f"The number {num} it's odd.")
    