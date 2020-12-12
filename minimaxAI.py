import sys
import math
import board

def minimax(state, humanSeed, compSeed, depth):
    def isTerminalState(state):
        eval = evaluation(state, humanSeed, compSeed)
        return eval

    def minVal(state, depth):
        if depth_limit:
            if depth >= depth_limit:
                return evaluation(state, humanSeed, compSeed)
        if isTerminalState(state):
            return evaluation(state, humanSeed, compSeed)

        min_utility = math.inf
        for col, sucState in board.find_successors(state):
            min_utility = min(min_utility, maxVal(sucState, depth + 1))
        return min_utility

    def maxVal(state, depth):
        if depth_limit:
            if depth >= depth_limit:
                return evaluation(state, humanSeed, compSeed)
        if isTerminalState(state):
            return evaluation(state, humanSeed, compSeed)

        max_utility = -math.inf
        for col, sucState in board.find_successors(state):
            max_utility = max(max_utility, minVal(sucState, depth + 1))
        return max_utility
    if depth:
        if depth == 0:
            return evaluation(state, humanSeed, compSeed)
    depth_limit = depth
    if board.find_next_player(state) == 1:
        return minVal(state, 1)
    return maxVal(state, 1)

def evaluationHelper(state, humanSeed, compSeed, row1, col1, row2, col2, row3, col3):
    score = 0;
    cells = state
    if cells[row1][col1] == compSeed:
        score = 1
    elif cells[row1][col1] == humanSeed:
        score = -1

    if cells[row2][col2] == compSeed:
        if score == 1:
            score = 10
        elif score == -1:
            return 0
        else:
            score = 1

    elif cells[row2][col2] == humanSeed:
        if score == -1:
            score = -10
        elif score == 1:
            return 0
        else:
            score = -1

    if cells[row3][col3] == compSeed:
        if score > 0:
            score *= 10
        elif score < 0:
            return 0
        else:
            score = 1

    elif cells[row2][col2] == humanSeed:
        if score < 0:
            score *= -10
        elif score > 1:
            return 0
        else:
            score = -1

    return score

def evaluation(state, humanSeed, compSeed):
    score = 0
    score += evaluationHelper(state, humanSeed, compSeed, 0, 0, 0, 1, 0, 2)
    score += evaluationHelper(state, humanSeed, compSeed, 1, 0, 1, 1, 1, 2)
    score += evaluationHelper(state, humanSeed, compSeed, 2, 0, 2, 1, 2, 2)
    score += evaluationHelper(state, humanSeed, compSeed, 0, 0, 1, 0, 2, 0)
    score += evaluationHelper(state, humanSeed, compSeed, 0, 1, 1, 1, 2, 1)
    score += evaluationHelper(state, humanSeed, compSeed, 0, 2, 1, 2, 2, 2)
    score += evaluationHelper(state, humanSeed, compSeed, 0, 0, 1, 1, 2, 2)
    score += evaluationHelper(state, humanSeed, compSeed, 0, 2, 1, 1, 2, 0)
    return score
