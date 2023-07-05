import numpy as np
from ...constants import BLACK, WHITE, MINIMAX_DEPTH
from ...formulations import available_moves_user, win


# Auxiliary function
def get_new_state(state, user, start, final):
    new_state = state.copy()
    
    new_state[start] = 0
    new_state[final] = user

    return new_state

# Evaluation function
# MAX -> White pieces
# MIN -> Black pieces
def evaluate(state):
    score = 0
    
    if win(state, WHITE):
        score = +1
    elif win(state, BLACK):
        score = -1

    return score

# Minimax algorithm

def minimax(state, depth=MINIMAX_DEPTH):
    value, movement = max_value(state, depth)

    return movement
    
def max_value(state, depth):
    value = evaluate(state)
    
    if value or not depth:
        return value, None

    max_eval = float('-inf')
    for action in available_moves_user(state, WHITE):
        cur_eval, _ = min_value(get_new_state(state, WHITE, *action), depth - 1)
        
        if cur_eval > max_eval:
            max_eval, movement = cur_eval, action
            
    return max_eval, movement

def min_value(state, depth):
    value = evaluate(state)
    
    if value or not depth:
        return value, None

    min_eval = float('inf')
    for action in available_moves_user(state, BLACK):
        cur_eval, _ = max_value(get_new_state(state, BLACK, *action), depth - 1)
        
        if cur_eval < min_eval:
            min_eval, movement = cur_eval, action
            
    return min_eval, movement
