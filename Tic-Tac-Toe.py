# requirements:
# 2 players should be able to play the game both sitting at the computer
# The board should be printed out everytime a player makes a move
# Take input form the player regarding the position and place a value within that position



import random

# display_board func: is used for displaying the board at any point of the game
def display_board(board):

    print("\n"*100)
    print(board[7]+'|'+board[8]+'|'+board[9])
    print("-----")
    print(board[4]+'|'+board[5]+'|'+board[6])
    print("-----")
    print(board[1]+'|'+board[2]+'|'+board[3])


# player_input func: is used for getting a user input which is either 'x' or 'O' only  
def player_input():
    
    user_input='wrong'

    while user_input.upper() not in ['X','O']:
        user_input=input("Player 1, Enter your choice either X or O: ")
        if user_input.upper() not in ['X','O']:
            print("Oops, invlaid entry. Enter a valid one")
    
    player1=user_input.upper()
    if player1=='X':
        player2='O'
    else:
        player2='X'

    return (player1,player2)


# place_marker function is used for placing the marker value at the desired position by the player
def place_marker(board,marker,position):
    
    board[position]=marker
    display_board(board)


# win check is a func which is used for checking whether any marker has won the game
def win_check(board,marker):
     
     # need to check for all rows if they are the same marker
     # need to check for all columns if they are the same marker
     # need to checl for diagonals if they are the same marker
     if((board[1]==marker and board[2]==marker and board[3]==marker)or
     (board[4]==marker and board[5]==marker and board[6]==marker)or
     (board[7]==marker and board[8]==marker and board[9]==marker)):
         return True
     elif((board[1]==marker and board[4]==marker and board[7]==marker)or
          (board[2]==marker and board[5]==marker and board[8]==marker)or
          (board[3]==marker and board[6]==marker and board[9]==marker)):
         return True
     elif((board[1]==marker and board[5]==marker and board[9]==marker)or
          (board[7]==marker and board[5]==marker and board[3]==marker)):
         return True
     else:
         return False



# choose_first decides which player goes first
def choose_first():
    flip=random.randint(0,1)
    if flip==0:
        return 'Player 1'
    else:
        return 'Player 2'
    

# space_check is used for checking wheter the position on the board is freely available
def space_check(board,position):
    return board[position]==' '


# full_board_check is used for checking whether the board is full or not
def full_board_check(board):
    return ' ' not in board
    
#player_position_choice is used for checking the validity of the postion chosen by the player      
def player_position_choice(board):
    position_list=[1,2,3,4,5,6,7,8,9]
    position_choice=100
    
    while position_choice not in position_list or not space_check(board,position_choice):
        position_choice=int(input("Enter a position form 1 to 9: "))
        if position_choice not in position_list:
            print("Oops invalid position. Enter a valid one- Or either the space is not freely available")
        
    return position_choice


#replay function is used whether the player chooses to replay the game or not
def replay():
    choice=input("Want to play the game again? Enter Y or N: ")
    return choice.upper()=='Y'



#GAME LOGIC

print("Welcome to tic-tac-toe game")

while True:
    print("Play the game! Good luck")
    #creating the board set_up
    board=[' ']*10
    display_board(board)
    #setting up the marker choices and the player turns
    player1_marker,player2_marker=player_input()
    first_player=choose_first()
    if first_player=='Player 1':
        print("Player 1 goes first")
        first_player=player1_marker
        second_player=player2_marker
    else:
        print("Player 2 goes first")
        first_player=player2_marker
        second_player=player1_marker
    result=False
    #game play
    while not full_board_check(board):
        
        position=player_position_choice(board)
        place_marker(board,first_player,position)
        if win_check(board,first_player):
            display_board(board)
            print(f'Player {first_player} wins')
            result=True
            break
        else:
            display_board(board)

        position=player_position_choice(board)
        place_marker(board,second_player,position)
        if win_check(board,second_player):
            display_board(board)
            print(f'Player {second_player} wins')
            result=True
            break
        else:
            display_board(board)

    if result==False:
        print("No player wins, It is a draw!")

    if not replay():
        break
