import random

choicee=["Rock","Paper","Scissor"]
while(True):
    print("This is Rock Paper Scissor Game")
    userwin,computerwin=0,0
    for i in range(1,6):
        print("Start round",i)
        print("Please enter any one option")
        print("1.Rock","2.Paper","3.Scissor",end="\n")

        # User can take the input (Rock/Paper/Scissor)
        user_choice=int(input())
        if(user_choice == 1):
            print("you select Rock")
            user_choice="Rock"
        elif(user_choice == 2):
            print("you select Paper")
            user_choice="Paper"
        elif(user_choice == 3):
            print("you select Scissor")
            user_choice="Scissor"
        else:
            print("Invalid selection")
            break
        # Computer can take random input (Rock/Paper/Scissor)
        comp_choice=random.choice(choicee)
        print("Computer choice",comp_choice)

        if(user_choice==comp_choice):
            print("This round id draw")
        elif(user_choice=="Rock" and comp_choice=="Scissor" or user_choice=="Scissor" and comp_choice=="Paper" or user_choice=="Paper" and comp_choice=="Rock"):
            print("Winner is user!")
            userwin+=1
        else:
            print("Winner is computer!")
            computerwin+=1
        
    if(userwin>computerwin):
        print("User is win the game!")
        print("Score is :","User score",userwin,"Computer score",computerwin,sep="")
    elif(computerwin>userwin):
        print("Computer is win the game")
        print("Score is :","User score :",userwin," Computer score : ",computerwin,sep="")
    else:
        print("Match is Draw")
        print("Score is :","User score",userwin,"Computer score",computerwin,sep="")

    choice=input("You want to play again?(Yes or No)")
    if(choice=='yes'or choice=='Yes'or choice=='YES'):
        continue
    else:
        print("Thanks for playing the Game",sep="\n")
        break