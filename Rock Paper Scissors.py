from random import randint 

rps = ["Rock", "Paper", "Scissors"]
com = rps[randint(0,2)]

player = False

while player == False:
    player = input("Rock!\nPaper!\nScissors!\n")
    if player == com:
        print("Tie")
    elif player == "Rock":
        if com == "Paper":
            print("YOU LOSE! Paper covers Rock")
        else:
            print("YOU WIN! Rock smashes Scissors")
    elif player == "Paper":
        if com == "Scissors":
            print("YOU LOSE! Scissors cuts Paper")
        else:
            print("YOU WIN! Paper covers Rock")
    elif player == "Scissors":
        if com == "Rock":
            print("YOU LOSE! Rock smashes Scissors")
        else:
            print("YOU WIN! Scissors cuts Paper")
    else:
        print("DO YOU KNOW HOW TO SPELL?!")
player = False
computer = rps[randint(0,2)]
        
