print("...Rock...")
print("...Paper...")
print("...Scissor...")
def game_play():
    player_input = input("Enter your move - Rock/Paper/Scissors : ").lower()
    from random import randint
    computer_move = randint(0,2)
    if computer_move == 0:
        computer = "rock"
    elif computer_move == 1:
        computer = "paper"
    else:
        computer = "scissors"
    print("Computer's Move is, ", computer)
    if player_input == computer:
        print("It's a tie.")
    elif player_input == "rock":
        if computer_move == 1:
            print("Paper wraps Rock, Computer Wins!!!")
        else:
            print(f"Rock breaks Scissors, Player Wins!!!")
            pass
    elif player_input[0] == "paper":
        if computer_move == 0:
            print(f"Paper wraps Rock, Player Wins!!!")
        else:
            print("Scissors cut Paper, Computer Wins!!!")
            pass
    elif player_input[0] == "scissor":
        if computer_move == 0:
            print("Rock can break Scissors, Computer Wins!!!")
        elif computer_move == 1:
            print(f"Scissors can cut Paper, Player Wins!!!")
    else:
        print("Thanks for playing. :)")
start_input = input("Do You want to start the game ? (Yes/No)? ")
if start_input == "Yes" or start_input == "yes":
    game_play()
else:
    print("Thank You!")
while(True):
    retry_input = input("Press Q to Exit or Y to Continue.(Q/Y)?  ")
    if retry_input[0] == "Q" or retry_input[0] == "q":
        exit()
    elif retry_input[0] == "Y" or retry_input[0] == "y":
        game_play()
    else:
        print("Please Give Valid Input")