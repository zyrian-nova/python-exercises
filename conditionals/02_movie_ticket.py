"""
Create a program that calculates the price of a movie ticket based on age:
Children under 12 pay $10.
Seniors (65 and older) pay $8.
Everyone else pays $12.
Example Output:

Enter your age: 70
Ticket price: $8
"""
REGULAR = 12
CHILDREN = 10
SENIOR = 8

print("Welcome to the cinema!")
age = int(input("Please enter your age: "))

if age <= 12:
    print(f"Ticket price: {CHILDREN}")
elif age >= 65:
    print(f"Ticket price: {SENIOR}")
else:
    print(f"Ticket price: {REGULAR}")
