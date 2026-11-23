# Hailey Wilson
# 11/23/26
# Secret word
# Stores a secret word, then asks for a guess and tells the user if it was correct.

SECRET = "python"

guess = input("Guess the word: ").lower()

if guess == SECRET:
    print("Correct!")
else:
    print("Wrong guess.")
