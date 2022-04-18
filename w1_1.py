from multiprocessing import parent_process


name1=input("Player 1:")
name2=input("Player 2:")
player_1=0
player_2=0
rock=int(0)
paper=int(1)
scissors=int(2)
i=1
while i<=4:
    print("Rock Paper Scissors?")

    choice1=int(input("Choice1:"))
    choice2=int(input("Choice2:"))

    if choice1==0:
        if choice2==0:
            player_1=player_1+0
            player_2=player_2+0
        elif choice2==1:
            player_2=player_2+1
        elif choice2==2:
            player_1=player_1+1


    if choice1==1:
        if choice2==1:
            player_1=player_1+0
            player_2=player_2+0
        elif choice2==2:
            player_2=player_2+1
        elif choice2==0:
            player_1=player_1+1


    if choice1==2:
        if choice2==2:
            player_1=player_1+0
            player_2=player_2+0
        elif choice2==0:
            player_2=player_2+1
        elif choice2==1:
            player_1=player_1+1

    i=i+1

print("name1---> {} player1---> {}  name2---> {}  player2---> {}".format(name1,player_1,name2,player_2))
if player_1 > player_2:
    print("{} won".format(name1))
elif player_1 == player_2:
    print("Game ended in a draw!!!")
else:
    print("{} won".format(name2))