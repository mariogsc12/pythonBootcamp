# DAY 7 - HANGMAN

import random

"""
--- TODO-1
- Create a variable called lives to keep track of the number of lives left
- Set lives to equal 5

--- TODO-2
- If guess is not a letter in the chosen_word. Then reduce lives by 1
- If lives goes down to 0 then the game should end, and it should print "YOU LOSE"

--- TODO-3
- print the ASCII art from the list stages that corresponds to the current number of lives the user has remaining
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

word_list = ["schedule", "behaviour", "beautiful"]
chosen_word = random.choice(word_list)

game_over = False
correct_letters = []
result = False
lives = 5
while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""
    print("Your guess is: " + guess)
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

    if result == False:
        lives-=1
        if lives == 0:
            game_over = True
            print("YOU LOSE")
            print("The word is: "+chosen_word)
    result = False
    
    if "_" not in display:
        game_over = True
        print("YOU WIN")
    
    print(stages[5-lives])
    




