import random

exit = False
user_points = 0
computer_points = 0

while exit == False:
    options = ["rock" , "paper" , "scissors"]
    user_input = input("Please Choose One Option or Exit: ")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Game Ended")
        exit = True
    
    if user_input == "rock":
        if computer_input == "rock":
            print("Your Input is Rock")
            print("Computer Input is Rock")
            print("It is a Tie!")
        elif computer_input == "paper":
            print("Your Input is Rock")
            print("Computer Input is Paper")
            print("Computer Wins!")
            computer_points += 1
        elif computer_input == "scissors":
            print("Your Input is Rock")
            print("Computer Input is scissors")
            print("You Wins!")
            user_points += 1

    elif user_input == "paper":
        if computer_input == "rock":
            print("Your Input is Paper")
            print("Computer Input is Rock")
            print("You Win")
            user_points += 1
        elif computer_input == "paper":
            print("Your Input is Paper")
            print("Computer Input is Paper")
            print("Tie!")
        elif computer_input == "scissors":
            print("Your Input is Paper")
            print("Computer Input is scissors")
            print("Computer Wins!")
            computer_points += 1

    elif user_input == "scissors":
        if computer_input == "rock":
            print("Your Input is scissors")
            print("Computer Input is Rock")
            print("Computer Win")
            computer_points += 1
        elif computer_input == "paper":
            print("Your Input is scissors")
            print("Computer Input is Paper")
            print("You Win")
            user_points +=1
        elif computer_input == "scissors":
            print("Your Input is scissors")
            print("Computer Input is scissors")
            print("Tie!")