import random
## How many rounds does user want to play
def game_mode(rounds):
    try:
        ## 3 rounds
        if (rounds == 3):
            print("Best out of 3!\n")
            ## 2 wins required to win
            win_in = 2
        ## 5 rounds
        elif (rounds == 5):
            print("Best out of 5!\n")
            ## 3 wins required to win
            win_in = 3
        else:
            print("INVALID! Either 3 or 5 rounds")
    except:
        print("Invalid Input!\nEnter 3 or 5 to select number of rounds\n")

    return win_in    

#CPU turn
def CPU_play():
    x = random.randint(1, 3)
    ##Randomly generate an option between rock, paper, or scissors
    if (x == 1):
        CPU = "ROCK"
    elif (x == 2):
        CPU = "PAPER"
    else:
        CPU = "SCISSORS"

    return CPU


def play(choice, opponent, user_score, CPU_score):
    ##check if user beat the CPU
    if (choice == "ROCK"):
        print("CPU played", opponent, "\n")
        if (opponent == "ROCK"):
            print("Draw\n")
        elif (opponent == "PAPER"):
            print("CPU wins round!\n")
            CPU_score += 1
        elif (opponent == "SCISSORS"):
            print("You win this round\n")
            user_score += 1
    elif (choice == "PAPER"):
        print("CPU played", opponent, "\n")
        if (opponent == "ROCK"):
            print("You win this round\n")
            user_score += 1
        elif (opponent == "PAPER"):
            print("Draw\n")
        elif (opponent == "SCISSORS"):
            print("CPU wins round!\n")
            CPU_score += 1
    elif (choice == "SCISSORS"):
        print("CPU played", opponent, "\n")
        if (opponent == "ROCK"):
            print("CPU wins round!\n")
            CPU_score += 1
        elif (opponent == "PAPER"):
            print("You win this round\n")
            user_score += 1
        elif (opponent == "SCISSORS"):
            print("Draw\n")
        

    return user_score, CPU_score

def winner(user_score, CPU_score, win_in):
    ## determine the winner depending on the number of rounds
    if (user_score == win_in):
        ##Show score
        print("User:", user_score, "\nCPU:", CPU_score, "\nCONGRATULATIONS! You win\n")
        return True
    elif (CPU_score == win_in):
        ##Show score
        print("User:", user_score, "\nCPU:", CPU_score, "\nGAME OVER\nBetter luck next time. Try again?\n")
        return True
    else:
        return False

def main():
    print("WELCOME TO ROCK PAPER SCISSORS.\n\nEnter Q at anytime to quit and R to restart\n")
    while True:
        ##Error handling user input to collect appropriate input
        try:
            round_count = int(input("How many rounds do you wish to play.\nEnter 3 or 5 for No.of.rounds: "))
            to_win = game_mode(round_count)
        except:
            print("Invalid input\n")
        else:
            break
    user_score = 0
    CPU_score = 0
    while True:
        response = input("Rock, Paper, Scissors, shoot!: ")
        response = response.upper()
        ##Enable user to quit the game
        if (response == "Q"):
            print("Bye!\n")
            break
        ##Enable user to start a new game
        elif (response == "R"):
            print("NEW GAME\n")
            user_score = 0
            CPU_score = 0
        ##Check for who won the round
        else:
            user_score, CPU_score = play(response, CPU_play(), user_score, CPU_score)
            check_winner = winner(user_score, CPU_score, to_win)
            if (check_winner):
                ##Prompt user to start a new game or end game
                while True:
                    ##Ensure User enters a valid input
                    try:
                        new = input("Enter Q for Quit or R to Restart: ")
                        new = new.upper()
                        if (new == "Q" or new == "R"):
                            response = new
                        else:
                            raise
                    except:
                        print("Invalid!\n")
                    else:
                        break
                if (response == "R"):
                    print("\nNEW GAME\n")
                    user_score = 0
                    CPU_score = 0
                elif (response == "Q"):
                    print("Bye!\n")
                    break
        

main()
