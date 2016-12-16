

board = [' ']*10
player_turn = 'Player 1'
player_one_turn = True
winner = False


def user_input():
    # ask for user input
  
    global player_turn
    global player_one_turn
    player_position = input(player_turn + ' choose position (1-9):')
    place_mark_on_board(player_turn, player_position)
  
  # change players on input
    if player_one_turn:
        player_turn = 'Player 2'
        player_one_turn = False
    else:
        player_turn = 'Player 1'
        player_one_turn = True        

def draw_board():
    global board
    # get all positions and draw the board
    print '---|---|---'
    print ' {} | {} | {} '.format(board[1], board[2], board[3])
    print '---|---|---'
    print ' {} | {} | {} '.format(board[4], board[5], board[6])
    print '---|---|---'
    print ' {} | {} | {} '.format(board[7], board[8], board[9])
    print '---|---|---'


def place_mark_on_board(player_turn, player_position):
    # check if position available
    # if yes -> place mark
    # if not -> return error
    # update state of board
    print '{} placed mark on position: {}'.format(player_turn, player_position)
    marker = 'X'
    global board
    global player_one_turn

    if not player_one_turn:
        marker = 'O'
        
    board[player_position] = marker
    draw_board()


for i in range(3):
    user_input()