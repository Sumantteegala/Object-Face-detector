import sys
import math
from board import createGameBoard, display, find_winner, find_next_player, get_move, get_move_AI

def start_Game(player1, player2, current_state=None):
    if current_state is None:
        current_state = createGameBoard(3, 3)
    print(display(current_state))

    turn = 0
    while find_winner(current_state) is None:
        if find_next_player(current_state) == 1:
            if player1 == 'c':
                compSeed = 'X'
                move, current_state = get_move_AI(current_state, humanSeed, compSeed)
            else:
                humanSeed = 'X'
                move, current_state = get_move(current_state)
        else:
            if player2 == 'c':
                compSeed = 'O'
                move, current_state = get_move_AI(current_state, humanSeed, compSeed)
            else:
                humanSeed = 'O'
                move, current_state = get_move(current_state)

        print(display(current_state))
        winner = find_winner(current_state)
        if winner == 0:
            print("No one wone. Game tie")
        elif winner == 1:
            print("Player 1 won the game")
        elif winner == -1:
            print("Player 2 won the game")
        turn+=1

def main():
    print('Welcome to TIC-TAC-TOE.')
    p = 'Play against robot(press c) or friend(press h)?'
    ins = input(p)
    if ins == 'c':
        p1 = 'Do u want to make the first move in the battle? (Y/N)'
        ins1 = input(p1)
        if ins1 == 'Y' or ins1 == 'y':
            start_Game('h', 'c')
        else:
            start_Game('c', 'h')
    else:
        start_Game('h', 'h')

if __name__ == "__main__":
    main()
