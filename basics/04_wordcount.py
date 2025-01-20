# Familiarize yourself with strings and Python's built-in functions.
# Instructions:
# 1. Ask the user for a sentence.  
# 2. Count how many words are in the sentence (words are separated by spaces).
phrase = input("Write a phrase: ")
words = phrase.split() #This divides the phrase into words
print(f"The phrase has {len(words)} words.")
