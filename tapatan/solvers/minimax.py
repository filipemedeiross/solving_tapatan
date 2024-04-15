from ..constants import BLACK, \
                        WHITE, \
                        MINIMAX_DEPTH
from ..formulations import get_moves, win


def get_state(grid, user, start, final):
    state = grid.copy()

    state[start] = 0
    state[final] = user

    return state

def evaluate(state):
    if win(state, WHITE):
        return +1
    elif win(state, BLACK):
        return -1

    return 0

def minimax(state, depth=MINIMAX_DEPTH):
    return max_value(state, depth)[1]

def max_value(state, depth):
    value = evaluate(state)

    if value or not depth:
        return value, None

    max_eval = float('-inf')
    for move in get_moves(state, WHITE):
        eval, _ = min_value(get_state(state, WHITE, *move), depth-1)

        if eval > max_eval:
            max_eval, max_move = eval, move

    return max_eval, max_move

def min_value(state, depth):
    value = evaluate(state)

    if value or not depth:
        return value, None

    min_eval = float('inf')
    for move in get_moves(state, BLACK):
        eval, _ = max_value(get_state(state, BLACK, *move), depth-1)

        if eval < min_eval:
            min_eval, max_move = eval, move

    return min_eval, max_move
