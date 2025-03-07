# DAY 7 - HANGMAN

import random

"""
--- TODO-1
- If the user has entered a letter they've already guessed, print the letter and let them know
- We should not deduct a life for this

--- TODO-2
- If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.

--- TODO-3
- Update the code to tell the user how many lives they have left
"""

stages = [''' 
=============
    +---+
    |   |
        |
        |
        |
        |
=============
''', ''' 
=============
    +---+
    |   |
    O   |
        |
        |
        |
=============
''', ''' 
=============
    +---+
    |   |
    O   |
    |   |
        |
        |
=============
''', ''' 
=============
    +---+
    |   |
    O   |
   /|\  |
        |
        |
=============
''', ''' 
=============
    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
=============
''', ''' 
=============
    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
=============
''']

# General game variables (modify to change the game rules)
word_list = ["schedule", "behaviour", "beautiful"]
lives = 5

# Variables used in the game's backend
game_over = False
result = False
placeholder = ""
correct_letters = []
used_letters = []
chosen_word = random.choice(word_list)

# Start the game logic
for letter in chosen_word:
    placeholder += "_"

print("----------- HANGMAN -----------")
print("Word to guess: " + placeholder)

while not game_over:

    guess = input("Guess a letter: ").lower()
    if len(guess)>1:
        print("ERROR - Invalid format")
    else: 
        print("Your guess is: " + guess)
        
        if guess in used_letters:
            print("----- You have already guessed " + guess + " -----")
            result = True
        if guess not in chosen_word:
            print("----- The letter " + guess + " is not in the word. Try again! -----")
        
        used_letters.append(guess)
        
        # Fill the displayed word
        display = ""
        for letter in chosen_word:
            if guess == letter:
                display += letter
                correct_letters.append(letter)
                result = True
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

        print(display)

        # Decrease the lives and print it (TODO-3)
        if result == False:
            lives-=1
        
        print("\n ----- You have " + str(lives) + " lives left ----- \n")
        
        # Check if the game has ended
        if lives == 0:
            game_over = True
            print("YOU LOSE")
            print("The word is: "+chosen_word)
        
        if "_" not in display:
            game_over = True
            print("YOU WIN")
        
        print(stages[5-lives])
    
    # If the game continues, restore the loop variables
    result = False
    

    




