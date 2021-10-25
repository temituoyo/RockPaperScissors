import random
## How many rounds does user want to play
def game_mode(rounds):
    try:
        ## 3 rounds
        if (rounds == 3):
            print("Best out of 3!")
            ## 2 wins required to win
            win_in = 2
        ## 5 rounds
        elif (rounds == 5):
            print("Best out of 5!")
            ## 3 wins required to win
            win_in = 3
    except:
        print("Invalid Input!\nEnter 3 or 5 to select number of rounds")

    return win_in

#CPU turn
def CPU_play(select):
    x = random.randint(1, 3)
    if (x == 1):
        CPU = "ROCK"
    elif (x == 2):
        CPU = "PAPER"
    else:
        CPU = "SCISSORS"

    return CPU


def play(choice, opponent, user_score, CPU_score):
    if (choice == "ROCK"):
        if (opponent == "ROCK"):
            print("Draw")
        elif (opponent == "PAPER"):
            CPU_score += 1
        elif (opponent == "SCISSORS"):
            user_score += 1
    elif (choice == "PAPER"):
        if (opponent == "ROCK"):
            user_score += 1
        elif (opponent == "PAPER"):
            print("Draw")
        elif (opponent == "SCISSORS"):
            CPU_score += 1
    elif (choice == "SCISSORS"):
        if (opponent == "ROCK"):
            CPU_score += 1
        elif (opponent == "PAPER"):
            user_score += 1
        elif (opponent == "SCISSORS"):
            print("Draw")

    return user_score, CPU_score

def winner(user_score, CPU_score, win_in):
    if (user_score == win_in):
        print("You win")
    elif (CPU_score == win_in):
        print("Better luck next time. Try again?")

def main():
    return

##Incomplete
