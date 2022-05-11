
import random
print("Choose Rock, paper or scissor \n")
user = input("choose rock, paper or scissor \n")

options = [ "rock", "paper", "scissor"]
computer = random.choice(options)

print(f'You chose {user} and computer chose {computer} ')

if user == computer:
        print(f"Both player selected {user}.Its a tie!")
        
elif user == "rock":
        if computer == "scissor":
            print ("Rock smashes scissor. You win!")
        else:
            print("Paper covers rock. You lose!")
elif user == "paper":
        if computer == "rock":
            print("Paper covers rock.You win!")
        else:
            print("scissor cuts paper. You Lose!")
elif user == "scissor":
        if computer == "paper":
            print("scissor cuts paper.You win!")
        else:
            print("Rock smashes scissor. You Lose!")





