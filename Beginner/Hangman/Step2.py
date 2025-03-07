# DAY 7 - HANGMAN

import random

"""
--- TODO-1
- Create an empty string called placeholder
- For each letter in the chosen_word, add _ to placeholder
- So if the chosen_word was "apple", placeholder should be "_ _ _ _ _"

--- TODO-2
- Create an empty string called "display"
- Loop through each letter in the chosen_word
- If the letter at that position matches guess then reveal that letter in the display at that position
- Print display and you should see the guessed letter in the correct position
- But every letter is not a match is represented with "_"
"""

word_list = ["schedule", "behaviour", "beautiful"]
chosen_word = random.choice(word_list)
guess = input("Guess a letter: ").lower()
print(guess)

result = "Wrong"
placeholder = ""
display = ""
for letter in chosen_word:
    if guess == letter:
        result = "Right"
        display += letter
    else :
        display += "_"
    placeholder += "_ "

print(display)
print(result + " - The word is: " + chosen_word)