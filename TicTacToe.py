def user_input(board):
    '''
    User is prompted for a position to put his / her mark
    on the board. Simple check which user's turn it is
    '''

    global player_turn
    global player_one_turn
    player_position = input(player_turn + ' choose position (1-9):')
    place_mark_on_board(board, player_turn, player_position)

    if player_one_turn:
        player_turn = 'Player 2'
        player_one_turn = False
    else:
        player_turn = 'Player 1'
        player_one_turn = True


def draw_board(board):
    '''
    Clear the screen and draw board's current state
    '''
    print(chr(27) + "[2J")

    print ' ___.___.___'
    print '|   |   |   |'
    print '| {} | {} | {} |'.format(board[1], board[2], board[3])
    print '|___|___|___|'
    print '|   |   |   |'
    print '| {} | {} | {} |'.format(board[4], board[5], board[6])
    print '|___|___|___|'
    print '|   |   |   |'
    print '| {} | {} | {} |'.format(board[7], board[8], board[9])
    print '|___|___|___|'


def check_if_board_full(board):
    '''
    If no player won the game in 9 rounds, the game,
    should be stoped with no winner.
    '''

    for field in xrange(1, 10):
        if board[field] == ' ':
            return False
    return True


def place_mark_on_board(board, player_turn, player_position):
    '''
    Get the user answer and put the mark on the board if place
    not already reserved. Check what mark should be put X or O
    After each placement check if there was a winner move.
    '''
    print '{} placed mark on position: {}'.format(player_turn, player_position)
    marker = 'X'
    global player_one_turn

    if not player_one_turn:
        marker = 'O'

    if board[player_position] is ' ':
        board[player_position] = marker
    else:
        print 'Position already taken!'

    draw_board(board)
    check_for_winner(board, player_turn, marker)


def check_for_winner(board, player_turn, marker):
    '''
    Check all available winning combinations:
    Horizontally, vertically and diagonally
    If there is a winning combination, print the winner.
    '''

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

while True:
    board = [' '] * 10
    player_turn = 'Player 1'
    player_one_turn = True
    winner = False

    while not winner and not check_if_board_full(board):
        draw_board(board)
        user_input(board)
    else:
        print 'Game Over!'
        break