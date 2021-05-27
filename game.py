
import random
import os 
import dotenv

dotenv.load_dotenv()


PLAYER_NAME = os.getenv("PLAYER_NAME")


print("Welcome", PLAYER_NAME,"to Rock, Paper, Scissors, Shoot!")
print("-----------------------------")
user_choice = input("Please choose either 'rock', 'paper' or 'scissors':")
#print("USER CHOICE:", user_choice)


#if user_choice = "rock" or "paper" or "scissors":
if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("USER CHOICE:", user_choice)
else:
    print("OOPS, invalid input. Please try again.")    
    exit()

#validate options
valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("COMPUTER CHOICE:", computer_choice)


#determine the winner
if user_choice == computer_choice:
    print ("IT'S A TIE!")
elif user_choice == "rock":
    if computer_choice == "paper":
        print("COMPUTER WINS!")
    else:
        print("YOU WIN!")
elif user_choice == "paper":
    if computer_choice == "scissors":
        print("COMPUTER WINS!")
    else:
        print("YOU WIN!")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print("COMPUTER WINS!")
    else:
        print("YOU WIN!")



#ending message
print("-----------------------------------------------")
print("THIS IS THE END OF OUR GAME. PLEASE PLAY AGAIN.")
