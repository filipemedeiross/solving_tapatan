# Standard formulation of the tapatan game

def available_pos(tapatan, x, y):
    position = []
    
    for pos in tapatan.moves[x][y]:
        if not tapatan.grid[pos]:
            position.append(pos)

    return position

def available_moves_user(tapatan, user):
    moves = []

    for pos in tapatan.user_pos(user):
        moves.extend((pos, move)
                     for move in available_pos(tapatan, *pos))

    return moves
