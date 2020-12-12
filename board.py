import sys
import math
from minimaxAI import minimax

def createGameBoard(rows, cols):
    board = []
    for i in range(0, rows):
        temp = []
        for j in range(0, cols):
            temp.append(0)
        board.append(temp)
    return board

def find_winner(current_state):
    rows = len(current_state)
    cols = len(current_state)
    win = 3

    # check horizontals
    for i in range(rows):
        for j in range(cols - win + 1):
            sums = sum([ current_state[i][x] for x in range(j, j + win) ])
            if abs(sums) == win:
                return 1 if sums > 0 else -1

    # check verticals
    for i in range(cols):
        for j in range(rows - win + 1):
            sums = sum([current_state[y][i] for y in range(j, j + win) ])
            if abs(sums) == win:
                return 1 if sums > 0 else -1

    if checkDiagonal(current_state) == 1:
        return 1

    # see if its empty
    for i in range(rows):
        for j in range(cols):
            if current_state[i][j] == 0:
                return None
    return 0

def display(board):
    output = { -1: "O", 1: "X", 0: "-" }
    string = ""
    for i in range(len(board)-1, -1, -1):
        string += "\n"
        for j in range(0, len(board[i])):
            string += "  " + output[board[i][j]]
    return string

def create_next_state(state, i):
    player = find_next_player(state)
    next_state = []
    next_state = createGameBoard(3, 3)
    for r in range(3):
        for c in range(3):
            next_state[r][c] = state[r][c]
    j = 0
    while (next_state[j][i] != 0) and (j < len(next_state)-1):
        j += 1
    next_state[j][i] = player
    return next_state

def find_successors(state):
    move_states = []
    cols = len(state[0])
    rows = len(state)
    for col in range(cols):
        if state[rows-1][col] == 0:
            move_states.append((col, create_next_state(state, col)))
    return move_states

def find_next_state(state, i, j):
    player = find_next_player(state)
    move_states = None
    if state[i][j] == 0:
        move_states = state[:]
        move_states[i][j] = player
    return move_states

def checkHorizontal(current_state):
    for i in range(rows):
        for j in range(cols - win + 1):
            sums = sum([ current_state[i][x] for x in range(j, j + win) ])
            if abs(sums) == win:
                return 1 if sums > 0 else -1
    return 0

def checkVertical(current_state):
    for i in range(cols):
        for j in range(rows - win + 1):
            sums = sum([current_state[y][i] for y in range(j, j + win) ])
            if abs(sums) == win:
                return 1 if sums > 0 else -1
    return 0

def checkDiagonal(current_state):
    # left diagonal
    for i in range(0, 1):
        for j in range(0, 1):
            if current_state[i][j] != 0 and current_state[i+1][j+1] == current_state[i][j] and current_state[i+2][j+2] == current_state[i][j]:
                return 1 if current_state[i][j] > 0 else -1

    # right diagonal
    for i in range(0, 1):
        for j in range(1, 3):
            if current_state[i][j] != 0 and current_state[i+1][j-1] == current_state[i][j] and current_state[i+2][j-2] == current_state[i][j]:
                return 1 if current_state[i][j] > 0 else -1
    return 0


def find_next_player(current_state):
    return 1 if sum(sum(current_state, [])) == 0 else -1

def get_move(state):
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    prompt = "Please enter your move {}: ".format(arr)
    move = int(input(prompt))
    if move == 1:
        i = 2
        j = 0
    elif move == 2:
        i = 2
        j = 1
    elif move == 3:
        i = 2
        j = 2
    elif move == 4:
        i = 1
        j = 0
    elif move == 5:
        i = 1
        j = 1
    elif move == 6:
        i = 1
        j = 2
    elif move == 7:
        i = 0
        j = 0
    elif move == 8:
        i = 0
        j = 1
    elif move == 9:
        i = 0
        j = 2
    next_state = find_next_state(state, i, j)
    return move, next_state

def get_move_AI(state, humanSeed, compSeed, depth=1):
    nextp = find_next_player(state)
    best_util = -math.inf if nextp == 1 else math.inf
    best_move = None
    best_state = None

    for move, state in find_successors(state):
        util = minimax(state, humanSeed, compSeed, depth)
        if ((nextp == 1) and (util > best_util)) or ((nextp == -1) and (util < best_util)):
            best_util, best_move, best_state = util, move, state
    return best_move, best_state
