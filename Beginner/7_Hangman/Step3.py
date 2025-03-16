# DAY 7 - HANGMAN

import random

"""
--- TODO-1
- Use a while loop to let the user guess again
- The loop should only stop once the user has guessed all the letters in the chosen_word
- At that point display has no more blanks. Then you can tell te user they've won

--- TODO-2
- Update the for loop so that previous guesses are added to the display String
- At the moment when the user makes a new guess, the previous guess gets replaced by a "_". We need to fix that by updating the for loop.
"""

word_list = ["schedule", "behaviour", "beautiful"]
chosen_word = random.choice(word_list)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""
    print("Your guess is: " + guess)
    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)
    
    if "_" not in display:
        game_over = True
        print("YOU WIN")



