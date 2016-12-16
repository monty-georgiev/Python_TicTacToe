

board = []
player_turn = 'Player 1'


def user_input():
    # ask for user input
    # change players on input
    global player_turn
    player_position = input(player_turn + 'choose position (1-9):')

    if player_turn == 'Player 1':
        player_turn = 'Player 2'
    else:
        player_turn = 'Player 1'

    print player_position


def draw_board():
    # get all positions and draw the board
    pass


def place_mark_on_board():
    # check if position available
    # if yes -> place mark
    # if not -> return error
    # update state of board
    pass


print 3**2