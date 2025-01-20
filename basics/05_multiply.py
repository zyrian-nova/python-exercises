"""
Multiplication Table Generator
Work with loops to create a multiplication table.
Instructions:
Ask the user for a number.
Print the multiplication table for that number (from 1 to 10).
"""
number = int(input("Enter a number to generate its multiplication table: "))

for table in range(1,11):
    print(f"{number} x {table} = {number * table}")
