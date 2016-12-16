

board = [' '] * 10
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
 
    print '---|---|---'
    print ' {} | {} | {} '.format(board[1], board[2], board[3])
    print '---|---|---'
    print ' {} | {} | {} '.format(board[4], board[5], board[6])
    print '---|---|---'
    print ' {} | {} | {} '.format(board[7], board[8], board[9])
    print '---|---|---'


def place_mark_on_board(player_turn, player_position):
    print '{} placed mark on position: {}'.format(player_turn, player_position)
    marker = 'X'
    global board
    global player_one_turn

    if not player_one_turn:
        marker = 'O'

    board[player_position] = marker
    draw_board()
    check_for_winner(player_turn, marker)


def check_for_winner(player_turn, marker):
    global board
    global winner

    if ((board[1] == marker and board[2] == marker and board[3] == marker) or
        (board[4] == marker and board[5] == marker and board[6] == marker) or
        (board[7] == marker and board[8] == marker and board[9] == marker) or
        (board[1] == marker and board[4] == marker and board[7] == marker) or
        (board[2] == marker and board[5] == marker and board[8] == marker) or
        (board[3] == marker and board[6] == marker and board[9] == marker) or
        (board[1] == marker and board[5] == marker and board[9] == marker) or
            (board[3] == marker and board[5] == marker and board[7] == marker)):
        winner = True
        print '{} is the winner'.format(player_turn)

while not winner:
    user_input()
    