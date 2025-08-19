#Request to moves's player1 and player2
player1__move = str(input("Enter Player 1's move: "))
player2__move = str(input("Enter Player 2's move: "))

moves = ["rock", "paper", "scissors"] #List of valid moves

#Check if the moves are valid
if player1__move not in moves or player2__move not in moves:
    print("Invalid move! Please choose from rock, paper, or scissors.")
else: #Determine the winner
    if player1__move == player2__move:
        print("It's a tie!")
    elif (player1__move == "rock" and player2__move == "scissors") or \
         (player1__move == "paper" and player2__move == "rock") or \
         (player1__move == "scissors" and player2__move == "paper"):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

#End of the game
print("Thank you for playing!")

