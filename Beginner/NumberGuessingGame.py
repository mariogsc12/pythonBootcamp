# DAY 12 FINAL PROJECT - NUMBER GUESSING GAME

import random 
import art 

class NumberGuessingGame:
    def __init__(self):
        self.attempts = 0
        self.remainingAttempts = 0
        self.difficulty = "empty"
        self.correctNumber = random.randint(1,100)
        self.endGame = False

    def initialize(self):
        art.tprint("Number  Guessing  Game")
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")

    def selectDifficulty(self):
        userInput = "empty"
        while userInput != "easy" and userInput != "hard":
            userInput = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

        self.difficulty = userInput
        if self.difficulty == "easy":
            self.attempts = 10
        elif self.difficulty == "hard":
            self.attempts = 5
        else:
            print("ERROR - Incorrect difficulty")


    def runGameLogic(self):
        self.remainingAttempts = self.attempts

        while self.remainingAttempts > 0 and self.endGame==False:
            print(f"You have {self.remainingAttempts} attempts remaining to guess the number.")
            try:
                guess = int(input("Make a guess: "))
                self.calculateResult(guess)
            except ValueError:
                print("You have introduced an invalid number. Please try again")

        if self.remainingAttempts == 0:
            print("You've run out of guesses, you lose.")
        else:
            print(f"You got it! The answer was {self.correctNumber}.")


    def calculateResult(self,guess):
        if guess == self.correctNumber:
            print(f"You got it! The answer was {self.correctNumber}.")
            self.endGame = True
        elif guess > self.correctNumber:
            print("Too high.")
            self.remainingAttempts -= 1
        else:
            print("Too low.")
            self.remainingAttempts -= 1

    # Wrapper for calling run function
    def __call__(self, *args, **kwds):
        self.run()

    def run(self):
        self.initialize()
        self.selectDifficulty()
        self.runGameLogic()
    


def main():
    NumberGuessingGame()()

if __name__ == "__main__":
    main()