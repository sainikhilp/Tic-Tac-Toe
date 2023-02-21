Specification requirements for developing Tic-Tac-Toe game application:
--> 2 players should be able to play the game both sitting at the computer 
--> The board should be printed out everytime a player makes a move 
--> Take input form the player regarding the position and place a value within that position

General Information: 
--> Player 1 and Player 2 are the name of the players playing the game 
--> marker = either 'X' or 'O' based on a player input or choice 
--> board = the tic-tac-toe grid 
--> List data structure is used for defining the board. 
--> The board game is visualized as number keypad

Visual representation of the board:

7 8 9 4 5 6 1 2 3

ADT used:

Board visualization and assignment :- --> display_board(board): this function takes board as an input 
parameter and displays the boad as a tic-tac-toe grid 
--> place_marker(board,marker,position)

Player Turn and their choice :- 
--> player_input(): this function assigns both the players a marker 
which is either 'X' or 'O' and returns the player choices 
--> choose_first(): this function decides which player goes choose_first --> player_position_choice(board): this function takes board as a paramter and takes a input from a player for assigning a marker. the chosen position is then validated whether it is freely available and the final position is returned.

Board and Result check: 
--> space-check(board,position): this function checks if the position is freely available in the board 
--> full_board_check(board): this function checks whether the board is full or not. 
--> win_check(board,marker): this function checks whether a particular player has won the game or not

Game Control: 
--> replay(): this function enbles to replay the game if the players wants to play the game again
