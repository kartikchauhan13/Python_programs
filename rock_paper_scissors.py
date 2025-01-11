import random

options = ("rock","paper","scissors")


playing = True
print("Python Rock Paper Scissors Game ")
while playing:
    player =None
    computer = random.choice(options)
    
    while player not in options:
        player =input("Enter a choice (rock / paper / scissors) :").lower()
    
    print(f"Your Choice : {player}")    
    print(f"Computer Choice : {computer}")
    if player == computer :
        print("Its a tie !!")
    elif player == "rock" and computer =="scissors":
        print("You win !!")
    elif player == "paper" and computer =="rock":
        print("You win !!")
    elif player == "scissors" and computer =="paper":
        print("You win !!")
    else :
        print("You lose :( ")
    play_again = input("Play again? (y/n) : ").lower()
    if play_again != "y":
        playing =False

print("Thanks for playing,have a good day!!")