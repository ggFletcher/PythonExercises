import random
options = ['r','p','c']
playerWins = 0
computerWins = 0
draws = 0

play = input("Would you like to play Rock Paper Scissors?(Y,y/N,n): ")
while play.lower() == 'y':
    playerMove = input("Enter your play (R - Rock, S - Scissors, P - Paper): ")
    computerMove = options[random.randrange(0,2)]
    print("\nYou chose      -", playerMove.upper())
    print("Computer chose -", computerMove.upper())

    if playerMove.lower() == 'r':
        if computerMove.lower() == 'r':
            print("You drew!")
            draws += 1
        elif computerMove.lower() == 'p':
            print("You lost!")
            computerWins += 1
        elif computerMove.lower() == 's':
            print("You won!")
            playerWins += 1
    elif playerMove.lower() == 'p':
        if computerMove.lower() == 'r':
            print("You won!")
            playerWins += 1
        elif computerMove.lower() == 'p':
            print("You drew!")
            draws += 1
        elif computerMove.lower() == 's':
            print("You lost!")
            computerWins += 1
    elif playerMove.lower() == 's':
        if computerMove.lower() == 'r':
            print("You lost!")
            computerWins += 1
        elif computerMove.lower() == 'p':
            print("You won!")
            playerWins += 1
        elif computerMove.lower() == 's':
            print("You drew!")
            draws += 1

    print("\n----- Scoreboard -----")
    print("Player wins   -", playerWins)
    print("Computer wins -", computerWins)
    print("Draws         -", draws)
    print("\n")

    play = input("play again?")
        
