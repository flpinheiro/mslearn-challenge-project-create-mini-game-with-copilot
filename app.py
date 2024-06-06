# write hello world to console
print("Hello World")

# Rock beats scissors.
# Scissors beat paper.
# Paper beats rock.
# If both players choose the same shape, the game is a tie.
# if player chooses a invalid shape, the game is invalid.
# The game should ask the player for their shape and then randomly select a shape for the computer.
# The game should then output the player's shape and the computer's shape, and then the result of the game.
# The game should then ask the player if they want to play again. If they do, the game should start over.
# If they don't, the game should exit.

import random



def get_player_choice():
    choice = input("Choose rock, paper, or scissors: ").lower()
    if choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return get_player_choice()
    return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        player_win += 1
        return "You win!"
    else:
        computer_win += 1
        return "You lose!"

def play_game():
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print(f"Your choice: {player_choice}, Computer's choice: {computer_choice}")
        print(determine_winner(player_choice, computer_choice))
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes" or play_again != "y":
            break
    
    
player_win: int = 0
computer_win: int = 0

if __name__ == "__main__":
    play_game()

    print("Thanks for playing!")
    print(f"Player wins: {player_win}, Computer wins: {computer_win}")