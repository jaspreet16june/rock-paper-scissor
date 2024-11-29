var computer_count = 0;
var player_count = 0;

function winner_of_rps(event){
    $.ajax({
        url: `http://localhost:8000/winner?player_choice=${event.target.id}`,
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
          },
        success: function(response) {
            if (response == "Oh ho!! It's a tie.."){
                alert(response)
                return
            }
            player = player_count + response.player_wins
            computer = computer_count + response.computer_wins
            $('#player-score').text(player)
            $('#computer-score').text(computer)
            player_count = player
            computer_count = computer
        },
        error: function(xhr, status, error) {
            
        }
    });
}