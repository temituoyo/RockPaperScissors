import random
## How many rounds does user want to play
def game_mode(rounds):
    try:
        if (rounds == 3):
            print("Best out of 3!")
            y = 3
        elif (rounds == 5):
            print("Best out of 5!")
            y = 5
    except:
        print("Invalid Input!\nEnter 3 or 5 to select number of rounds")

    return y

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


def score_count():
    
    return


##Incomplete
