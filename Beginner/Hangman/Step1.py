# DAY 7 - HANGMAN

import random

word_list = ["schedule", "behaviour", "beautiful"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)

# TODO-2 - Ask the user to guess a letter and assignanswer to a variable called guess. Make guess lowercase
guess = input("Guess a letter: ").lower()
print(guess)

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it is, "Wrong" if it's not.
result = "Wrong"

# -- In python we can iterate over a string --
for letter in chosen_word:
    if guess == letter:
        result = "Right"
# -- Other option based on C++ --
"""
for i in len(0,len(chosen_word)):
    if guess == chosen_word[i]:
        result = "Right"
"""

print(result + " - The word is: " + chosen_word)