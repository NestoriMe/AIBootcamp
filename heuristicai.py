import random
import game
import sys

# Author:				chrn (original by nneonneo)
# Date:				11.11.2016
# Description:			The logic of the AI to beat the game.

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
lastmove = -1

def find_best_move(board):
    bestmove = -1
    global lastmove    
	
	# TODO:
	# Build a heuristic agent on your own that is much better than the random agent.
	# Your own agent don't have to beat the game
    # bestmove = find_best_move_random_agent()

    if lastmove == UP:
        bestmove = DOWN
    elif lastmove == LEFT:
        bestmove = RIGHT
    else:

        bestmove = RIGHT
        
        if not does_it_work(bestmove, board):
            bestmove = DOWN
            if not does_it_work(bestmove, board):
                bestmove = UP
                if not does_it_work(bestmove, board):
                    bestmove = LEFT
    
    

    lastmove = bestmove
    return bestmove

def does_it_work(move, board):
    new_board = execute_move(move, board)
    if board_equals(new_board, board):
        return False
    else:
        return True

def find_best_move_random_agent():
    return random.choice([UP,DOWN,LEFT,RIGHT])
    
def execute_move(move, board):
    """
    move and return the grid without a new random tile 
	It won't affect the state of the game in the browser.
    """

    if move == UP:
        return game.merge_up(board)
    elif move == DOWN:
        return game.merge_down(board)
    elif move == LEFT:
        return game.merge_left(board)
    elif move == RIGHT:
        return game.merge_right(board)
    else:
        sys.exit("No valid move")
		
def board_equals(board, newboard):
    """
    Check if two boards are equal
    """
    return  (newboard == board).all()  