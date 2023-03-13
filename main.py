#!/usr/bin/env python3

def draw_board(board):
    #TODO: Define a function to draw the game board
    pass

def play(board, player, cell):
    # Check if cell is free
    # board['11'] = 'x'
    pass

def main():
    print("Hello World!")

    print("Hello Back!")

    # Define game board
    board = {'00': '', '01': '','02': '',
             '10': '', '11': '','12': '',
             '20': '', '21': '','22': ''}

    print("Game board:" + str(board))

    # Test the functions
    
    draw_board(board)
    
    play(board, 'x', '21')
    
    draw_board(board)

if __name__ == "__main__":
    main()