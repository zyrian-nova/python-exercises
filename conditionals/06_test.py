"""
An e-commerce website offers discounts based on the following criteria:

If the total purchase is above $100, apply a 10% discount.
If the total purchase is above $200, apply a 20% discount.
If the user is a "premium" member, they get an additional 5% discount on top of other discounts.
Write a program that:

Prompts the user for their total purchase amount and membership status (yes or no for "premium").
Calculates and displays the final price after applying any applicable discounts.
"""
discount = 0 # pylint: disable=invalid-name
membership_discount = 0 # pylint: disable=invalid-name

print("Welcome to the automatic purchase program!")

try:
    purchase = float(input("Please enter the total of your purchase: $"))
    if purchase < 0:
        print("Purchase amount cannot be negative.")
        exit()
except ValueError:
    print("Please enter a valid ammount. (E.g. $10.50)")
    exit()

membership = input("Are you a premium member? (Yes/No): ").strip().upper()
if membership not in {"YES", "NO"}:
    print("Invalid choice. Please enter a valid response. (E.g. Y/N).")
    exit()

if purchase >= 200:
    discount = purchase * 0.20
    total = purchase - discount
elif purchase >= 100:
    discount = purchase * 0.10
    total = purchase - discount
else:
    total = purchase

if membership == "YES":
    membership_discount = total * 0.05
    total -= membership_discount

print("\n--- Receipt ---")
print(f"Purchase: $ {purchase:.2f}")
if discount > 0:
    print(f"Discount: $ {discount:.2f}")
print(f"Premium membership: {membership}")
if membership == "YES":
    print(f"Membership discount: $ {membership_discount:.2f}")
print(f"Total: $ {total:.2f}")
