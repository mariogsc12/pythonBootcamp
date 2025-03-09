# DAY 11 FINAL PROJECT - BLACKJACK

"""
---- RULES ----
- The deck is unlimited in size (the probability is the same during all the game
)
- There are no jokers
- The Jack/Queen/King all count as 10
- The Ace can count as 11 or 1
- The cards in the list have equal probability of being drawn
- Cards are not removed from the deck as they are drawn
- The computer is the dealer
"""


import random
import art


# Function definitions
def deal_cards(deck_cards):
    game_cards = {}
    game_cards["user"]=[random.choice(deck_cards),random.choice(deck_cards)]
    game_cards["computer"]=[random.choice(deck_cards),random.choice(deck_cards)]

    return game_cards

def calculate_score(cards):
    """ Take a list of cards and return the score calculated from the cards"""
    score = sum(cards)
    if score==21 and len(cards) == 2: # BLACKJACK
        return 0    
    elif 11 in cards and score>21:        # If the player has an Ace and their total score goes over 21, the Ace’s value is changed to 1 instead of 11
        for _ in range(cards.count(11)):  # Loop through and convert Aces to 1
            cards.remove(11)
            cards.append(1)
        score = sum(cards)  # Recalculate score after converting Aces

    return score

def receive_user_input(message):
    while True:
        user_input = input(message).lower()
        if user_input in ('y','n'):
            return user_input
        else:
            print("ERROR - Please introduce 'y' or 'n'")

        
def compare(u_score, c_score):
    if u_score == c_score:
        message = "It's a draw."
    elif u_score == 0:
        message = "You win with a Blackjack!"
    elif c_score == 0:
        message = "You lose, opponent has a Blackjack."
    elif u_score > 21:
        message = "You went over 21. You lose."
    elif c_score > 21:
        message = "Opponent went over 21. You win!"
    elif u_score > c_score:
        message = "Congratulations! You win."
    else:
        message = "Computer is closer to 21. You lose."

    return message

def computer_turn(game_cards):
    """ Let the computer take turns drawing cards until it reaches a score of 17 or higher """
    computer_score = calculate_score(game_cards["computer"])
    while computer_score < 17:
        print("The computer draws another card.")
        game_cards["computer"].append(random.choice(cards))
        computer_score = calculate_score(game_cards["computer"])
    return computer_score


# Global variables
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
def play_game():
    game_cards = deal_cards(cards)   # Dictionary with the dealt cards
    is_game_over = False

    # User turn
    while not is_game_over:
        user_score = calculate_score(game_cards["user"])
        computer_score = calculate_score(game_cards["computer"])

        print(f"Your cards: {game_cards['user']}, current score: {user_score}")
        print(f"Computer's first card: {game_cards['computer'][0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = receive_user_input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                game_cards["user"].append(random.choice(cards))
            elif user_should_deal == 'n':
                is_game_over = True

    # Computer turn
    computer_score = computer_turn(game_cards)

    print(f"""
    ================================================
        {compare(user_score,computer_score)}
    ================================================
    """)
    print(f"Your final hand: {game_cards['user']}, final score {user_score}")
    print(f"Computer's final hand: {game_cards['computer']}, final score {computer_score}\n\n\n")



# GAME LOGIC
art.tprint("BLACKJACK")
while receive_user_input("Do you want to play another game of Blackjack? Type 'y' or 'n': ") == 'y':
    print("\n")
    play_game()

# END GAME
print("""
================================================
    Thank you for playing Mario's Blackjack. 
    See you again!
================================================
""")






