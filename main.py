# <------ ROCK PAPER SCISSOR ----->
import random
game_choices = ['rock', 'paper', 'scissor']


def select_choices():
    player_choice = input("Enter the choice please ('rock', 'paper', 'scissor'): ")
    computer_choice = random.choices(game_choices)
    user_choices = {
        'player': player_choice,
        'computer': computer_choice[0]
    }
    print(user_choices)
    
    return user_choices


def winner_of_rps(response):
    if (response['player'] == 'rock' and response['computer'] == 'scissor') or (response['player'] == 'paper' and response['computer'] == 'rock') or (response['player'] == 'scissor' and response['computer'] == 'paper'):
        return "Player wins!"
    
    elif response['player'] == response['computer']:
        return "Oh ho!! It's a tie.."
    
    return "Computer wins!"

print(winner_of_rps(select_choices()))