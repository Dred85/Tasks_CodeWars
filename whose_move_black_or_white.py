def whose_move(last_player, win):
    if win == True:
        return last_player
    else:
        if last_player == 'black':
            return 'white'
        else:
            return 'black'


# def whoseMove(lastPlayer, win):
#     players = ['white', 'black']
#     return lastPlayer if win else players[players.index(lastPlayer) - 1]

print(whose_move('white', False))

