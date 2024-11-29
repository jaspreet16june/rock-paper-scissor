# <------ ROCK PAPER SCISSORs ----->
import random
game_choices = ['rock', 'paper', 'scissors']


def select_choices():
    player_choice = input("Enter the choice please ('rock', 'paper', 'scissors'): ")
    computer_choice = random.choice(game_choices)
    user_choices = {
        'player': player_choice,
        'computer': computer_choice
    }    
    return user_choices


def winner_of_rps(response):
    player = response['player']
    computer = response['computer']
    
    print(f"You chose {player} and Computer chose {computer}")
    
    if player == computer:
        return "Oh ho!! It's a tie.."
    
    elif player == 'rock':
        if computer == 'scissors':
            return "Rock smashes Scissors! You win!"
        else:
            return "Paper covers the rock! You Lose!"
    
    elif player == 'paper':
        if computer == 'scissors':
            return "Scissor cuts the paper ! You Lose!"
        else:
            return "Paper covers the rock! You Win!"
       
    elif player == 'scissors':
        if computer == 'paper':
            return "Scissor cuts the paper ! You Win!"
        else:
            return "Rock smashes Scissors! You Lose!" 
        
print(winner_of_rps(select_choices()))