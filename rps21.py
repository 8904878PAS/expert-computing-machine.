from random import randint
t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0,2)]
while(True):
    player = input("r, p, s")
    if player == computer:
        print("Tie!")
    elif player == "r":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "p":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "s":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
        player = False
        computer = t[randint(0,2)]
