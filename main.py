# <------ ROCK PAPER SCISSORs ----->
from fastapi import FastAPI, Request
import random
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

origins = [
    "http://localhost:8000",  # Your frontend URL
    "http://localhost:5000",  # Another allowed frontend URL (if applicable)
]

# Add CORSMiddleware to the FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from the specified origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

game_choices = ['rock', 'paper', 'scissors']



@app.get('/winner/')
def winner_of_rps(requests:Request):
    
    player = requests.query_params.get('player_choice')

    computer = random.choice(game_choices)
    player_count = 0
    computer_count = 0
    message = ''
    
    print(f"You chose {player} and Computer chose {computer}")
    
    if player == computer:
        return "Oh ho!! It's a tie.."
    
    elif player == 'rock':
        if computer == 'scissors':
            player_count += 1
            message = "Rock smashes Scissors! You win!"
        else:
            computer_count +=1
            message = "Paper covers the rock! You Lose!"
    
    elif player == 'paper':
        if computer == 'scissors':
            computer_count +=1
            message = "Scissor cuts the paper ! You Lose!"
        else:
            player_count += 1
            message = "Paper covers the rock! You Win!"
       
    elif player == 'scissors':
        if computer == 'paper':
            player_count += 1
            message = "Scissor cuts the paper ! You Win!"
        else:
            computer_count +=1
            message = "Rock smashes Scissors! You Lose!" 
            
    return {
        "computer_wins": computer_count,
        "player_wins": player_count,
        "message": message
    }
        
        
# print(winner_of_rps(select_choices()))


