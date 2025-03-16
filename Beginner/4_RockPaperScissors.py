# DAY 4 FINAL PROJECT - ROCK PAPER SCISSORS

import random

def userChoice() -> int:
    user = int(input("Your turn!. Enter a number: 0->Rock, 1->Paper, 2->Scissors: "))
    while checkValidNumber(user)==False :
        user = int(input("Please enter a valid number: 0->Rock, 1->Paper, 2->Scissors: "))
    return user

def computerChoice() -> int:
    computer = random.randint(0,2)
    print(f"Opponent's turn! The choice is: {computer} ")
    return computer

def checkValidNumber(num) -> bool:
    if num >= 0 and num<=2:
        return True
    else :
        return False
    
def main():
    finalScore = 3
    computerScore = 0
    userScore = 0

    while computerScore<finalScore and userScore<finalScore:
        user = userChoice()
        computer = computerChoice()

        if user==1 and computer==0:
            userScore += 1
        elif user==2 and computer==1:
            userScore += 1
        elif user==0 and computer==2:
            userScore += 1
        elif user==0 and computer==1:
            computerScore += 1
        elif user==1 and computer==2:
            computerScore += 1
        elif user==2 and computer==0:
            computerScore += 1
        else:
            print("It is Draw!")

    if computerScore==finalScore:
        print("\n\nGAME OVER!\n\n")
        print(f"user: {userScore} - computer: {computerScore}")
    else:
        print("\n\nCongratulations! YOU WIN\n\n")
        print(f"user: {userScore} - computer: {computerScore}")

if __name__ == "__main__":
    main()
