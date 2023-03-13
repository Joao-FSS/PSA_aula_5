#!/usr/bin/env python3

def draw_board(board):
    #TODO: Define a function to draw the game board
    print('-------') #linha 1
    print('|'+ board['00']+ '|'+ board['01'] +'|'+ board['02']+ '|')
    print('-------') #linha 2
    print('|'+ board['10']+ '|'+ board['11'] +'|'+ board['12'] + '|')
    print('-------') #linha 3
    print('|'+ board['20']+ '|'+ board['21'] +'|'+ board['22'] + '|')
    print('-------') #linha 4


def play(board, player, cell):

    #verificação do jogador
    if not player == 'x' and not player== 'o':
        print('invalid player:' + player)
        return False
    

    # Check if cell is free
    if board[cell]== ' ' :
        board[cell] = player
        print(player + ' to cell ' + cell)
        return True
    else:
        print('invalid play, cell ' + cell +' is ocupied')
        return False


#TODO: check if board is full
def is_full(board):
    pass


#TODO: have winner
def have_winner(board)
    pass





def main():
    print("Hello World!")

    print("Hello Back!")

    # Define game board
    board = {'00': ' ', '01': ' ','02': ' ',
             '10': ' ', '11': ' ','12': ' ',
             '20': ' ', '21': ' ','22': ' '}

    print("Game board:" + str(board))

    # Test the functions
    
    draw_board(board)
    #TODO: create game mechanism
    play(board, 'x', '21')
    play(board, 'o', '11')
    play(board, 'x', '01')
    play(board, 'x', '21')
    
    draw_board(board)

if __name__ == "__main__":
    main()