user_choice = {}
user1 = input("Enter User Name 1 : ")
user2 = input("Enter User Name 2 : ")
score_user1 = 0
score_user2 = 0
while True:
    i = 0
    while i <= 10:
        user1_choice = input("Enter a choice (rock, paper, scissors): ")
        user2_choice = input("Enter a choice (rock, paper, scissors): ")
        user_choice[user1] = user1_choice
        user_choice[user2] = user2_choice
        print(user_choice)
        if  user1_choice ==  user2_choice:
            print("Both players selected" ,user1_choice,  " it a tie!")


            print(user1,'has',score_user1,'points and',user2,'has',score_user2,'points')
        elif  user1_choice == "rock":
            if  user2_choice == "scissors":
                print("Rock smashes scissors!", user1, "Gets 1 Point!")
                score_user1 = score_user1+1
                print(user1,'has',score_user1,'points and',user2,'has',score_user2,'points')
            else:
                print("Paper covers rock!", {user2}, "Gets 1 Point!")
                score_user2 = score_user2+1
                print(user1,'has',score_user1,'points and',user2,'has',score_user2,'points')
        elif user1_choice == "paper":
            if user2_choice == "rock":
                print("Paper covers rock!" , user1, "Gets 1 Point!")
                score_user1 = score_user1+1
                print(user1,'has',score_user1,'points and',user2,'has',score_user2,'points')
            else:
                print("Scissors cuts paper!" , user2, "Gets 1 Point!")
                score_user2 = score_user2+1
                print(user1,'has',score_user1,'points and',user2,'has',score_user2,'points')
        elif user1_choice == "scissors":
            if user2_choice == "paper":
                print("Scissors cuts paper!", user1, "Gets 1 Point!")
                score_user1 = score_user1+1
                print(user1,'has',score_user1,'points and',user2,'has',score_user2,'points')
            else:
                print("Rock smashes scissors!" , user2, "Gets 1 Point")
                score_user2 = score_user2+1
                print(user1,'has',score_user1,'points and',user2,'has',score_user2,'points')
        i+=1
    if score_user1 > score_user2:
        print(user1,"WINS!")
    elif score_user2 > score_user1:
        print(user2,"WINS THE GAME!")
    else:
        print("It's a tie!")
    play = input("Do you want to play again? Press Y for Yes, N for N0 --->")
    if play.upper() == "Y":
        i=0
        continue
    else:
        print("BYE")
        break
    