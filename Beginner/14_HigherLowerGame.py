# DAY 14 FINAL PROJECT - HIGHER LOWER GAME

import art
import random 

famous_person_db = {
    'Selena Gomez': {
        'name': 'Selena Gomez',
        'follower_count': 251000000,  
        'description': 'American singer, songwriter, and actress. Known for her roles in Disney\'s Wizards of Waverly Place and as a solo music artist.',
        'country': 'USA'
    },
    'Cristiano Ronaldo': {
        'name': 'Cristiano Ronaldo',
        'follower_count': 560000000,  
        'description': 'Portuguese professional footballer, widely considered one of the greatest players of all time.',
        'country': 'Portugal'
    },
    'Taylor Swift': {
        'name': 'Taylor Swift',
        'follower_count': 250000000,  
        'description': 'American singer-songwriter, known for narrative songs about her personal life.',
        'country': 'USA'
    },
    'Dwayne "The Rock" Johnson': {
        'name': 'Dwayne "The Rock" Johnson',
        'follower_count': 390000000,  
        'description': 'American actor, producer, and former professional wrestler. Known for roles in movies like Jumanji and Fast & Furious.',
        'country': 'USA'
    },
    'Kylie Jenner': {
        'name': 'Kylie Jenner',
        'follower_count': 400000000,  
        'description': 'American reality television personality, socialite, and businesswoman. Founder of Kylie Cosmetics.',
        'country': 'USA'
    },
    'Lionel Messi': {
        'name': 'Lionel Messi',
        'follower_count': 480000000,  
        'description': 'Argentine professional footballer, regarded as one of the greatest players in football history.',
        'country': 'Argentina'
    }
}


class HigherLowerGame:
    def __init__(self,db):
        self.name = "Higher Lower"
        self.score = 0
        self.database = db
        self.endGame = False

    def initialize(self):
        art.tprint(self.name + " Game")
    
    def runGameLogic(self):
        while self.endGame == False:
            optionA = random.choice(list(self.database.keys()))
            optionB = random.choice(list(self.database.keys()))

            while optionA == optionB: # Ensure that optionA and optionB are different
                optionB = random.choice(list(self.database.keys()))

            print(f"Compare A: {self.database[optionA]["name"]}, {self.database[optionA]["description"]}")
            print("-------------------- VS --------------------")
            print(f"Against B: {self.database[optionB]["name"]}, {self.database[optionB]["description"]}")
            
            userInput = "emtpy"
            while userInput != 'A' and userInput != 'B':
                userInput=input("Who has more followers? Type 'A' or 'B': ").upper()

            if (self.database[optionA]["follower_count"]>self.database[optionB]["follower_count"]):
                if userInput == 'A':
                    self.score += 1
                    print(f"Correct! You're score is {self.score}'\n\n")
                else:
                    self.endGame = True
            elif (self.database[optionA]["follower_count"]<self.database[optionB]["follower_count"]):               
                if userInput == 'B':
                    self.score += 1
                    print(f"Correct! You're score is {self.score}'\n\n")
                else:
                    self.endGame = True
            
        print(f"Sorry, that's wrong. Final score {self.score}")

    def run(self):
        self.initialize()
        self.runGameLogic()

    # Wrapper to call run function
    def __call__(self, *args, **kwds):
        self.run()

    
def main():
    HigherLowerGame(famous_person_db)()

if __name__ == "__main__":
    main()