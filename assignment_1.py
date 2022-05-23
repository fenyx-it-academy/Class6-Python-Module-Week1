# HOMEWORK_1
# Take the names of the players and play the stone - paper - scissors game.
# Game 10 hands it will last. At the end of 10 hands, the winner will be determined.
# The score will be displayed at the end.

player1 = input("Enter your name: ")
player2 = input("Enter your name: ")
scoreOfThePlayer1 = 0
scoreOfThePlayer2 = 0

i = 0
while i < 10:
    i +=1
    choice1 = input(player1 + "! Please choice your game: Stone, Paper or Scissors: ")
    choice2 = input(player2 + "! Please choice your game: Stone, Paper or Scissors: ")
    if choice1==choice2:
        print("No winner. Please try again")
    elif choice1 == "Stone":
        if choice2 == "Paper":
            print(player2, "won.")
            scoreOfThePlayer2 +=1
        else:
           print(player1, "won.") 
           scoreOfThePlayer1 +=1
    elif choice1 == "Paper":
        if choice2 == "Stone":
            print(player1, "won.")
            scoreOfThePlayer1 +=1
        else:
            print(player2, "won.") 
            scoreOfThePlayer2 +=1
    elif choice1 == "Scissors":
        if choice2 == "Stone":
            print(player2, "won.")
            scoreOfThePlayer2 +=1
        else:
            print(player1, "won.") 
            scoreOfThePlayer1 +=1

print(player1, "has totally", scoreOfThePlayer1, "points.")   
print(player2, "has totally", scoreOfThePlayer2, "points.")   

if scoreOfThePlayer1 > scoreOfThePlayer2:
    print(player1, "won the game. Congratulations!")
elif scoreOfThePlayer1 == scoreOfThePlayer2:
    print("Neither", player1, "nor", player2, "won!")
else:
    print(player2, "won the game. Congratulations!")


        

