"""
Write a program that:
Asks the user for a number.
Prints:
"Fizz" if the number is divisible by 3.
"Buzz" if the number is divisible by 5.
"FizzBuzz" if the number is divisible by both 3 and 5.
The number itself if it is divisible by neither.
Example Output:

Enter a number: 15
FizzBuzz
"""
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

if num % 5 == 0 and num % 3 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(f"The number {num} can't Fizz or Buzz.")
