#RagebaitRockPaperScissors
from time import sleep
print("Rock Paper Scissors")
gameStart = input("Do you want to play? (y/n) ")
while(gameStart != "y"):
    gameStart = input("Do you want to play? (y/n) ")
if(gameStart == "y"):
    print("Great! Lets get started!")
    sleep(1)
    print("You are playing against the computer. The first to 3 wins is the winner.")
    sleep(1)
    print("Rock beats scissors, scissors beats paper, and paper beats rock.")
    sleep(1)
    print("Good luck!")
    rps = input("Your choice: (r,p,s)")
    if(rps == "r"):
        print("Computer Choice: Paper")
        sleep(1)
        print("You lose!")
    elif(rps == "p"):
        print("Computer Choice: Scissors")
        sleep(1)
        print("You lose!")
    elif(rps == "s"):
        print("Computer Choice: Rock")
        sleep(1)
        print("You lose!")