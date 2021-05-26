
import random

print("Rock, Paper, Scissors, Shoot!")
user_choice = input("Please choose either 'rock', 'paper' or 'scissors':")
print("USER CHOICE:", user_choice)


#if user_choice = "rock" or "paper" or "scissors":
if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("VALID. KEEP GOING")
else:
    print("OOPS, invalid input. Please try again.")    
    exit()

valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("COMPUTER CHOICE:", computer_choice)


print("THIS IS THE END OF OUR GAME. PLEASE PLAY AGAIN.")
