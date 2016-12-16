

board = []
player_turn = 'Player 1'


def user_input():
    # ask for user input
  
    global player_turn
    player_position = input(player_turn + 'choose position (1-9):')

  

    place_mark_on_board(player_turn, player_position)
  # change players on input
      if player_turn == 'Player 1':
            player_turn = 'Player 2'
    else:
        player_turn = 'Player 1'


def draw_board():
    # get all positions and draw the board
    pass


def place_mark_on_board(player_turn, player_position):
    # check if position available
    # if yes -> place mark
    # if not -> return error
    # update state of board
    print '{} placed mark on position: {}'.format(player_turn, player_position)


user_input()