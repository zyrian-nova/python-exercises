"""
Write a program that validates a user’s password based on the following criteria:

It must be at least 8 characters long.
It must contain at least one uppercase letter, one lowercase letter, and one digit.
If the password is invalid, display the specific reason(s) why.
    (e.g., "Password must contain at least one uppercase letter").
If the password is valid, display "Password accepted."
"""
try:
    password = input("Enter the password to validate: ")

except ValueError:
    print("The password must be at least 8 characters long.")
    exit()

characters = password.split()

print(characters)
