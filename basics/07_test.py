"""
Write a program that checks if a given string is a palindrome.
Requirements:
Ask the user for a word or phrase.
Remove any spaces or special characters and make the input lowercase.
Check if the cleaned string is the same backward as forward.
Print whether it is a palindrome or not.
"""
text = input("Enter a word or a phrase: ")
text = text.replace(" ","")
TEXT = str.lower(text)
if TEXT == TEXT[::-1]:
    print("Yor word or text is a palindrome!")
else:
    print("Your word or text is not a palindrome.")
    print(f"Original text: {TEXT}")
    print(f"Reversed text: {TEXT[::-1]}") # Shows the reversed text
