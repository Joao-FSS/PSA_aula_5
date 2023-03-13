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



def is_full(board):
    num_occupied = 0
    cells = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
    for cell in cells:
        if not board[cell] == ' ':
            num_occupied += 1

    if num_occupied == 9:
        print('Board is full')
        return True
    else:
        return False



def have_winner(b):

    for p in ['x', 'o']:

        # Horizontal lines
        if b['00'] == p and b['01'] == p and b['02'] == p:
            print('Player ' + p + ' has won!!!')
            return p
        
        if b['10'] == p and b['11'] == p and b['12'] == p:
            print('Player ' + p + ' has won!!!')
            return p

        if b['20'] == p and b['21'] == p and b['22'] == p:
            print('Player ' + p + ' has won!!!')
            return p

        # Vertical lines
        if b['00'] == p and b['10'] == p and b['20'] == p:
            print('Player ' + p + ' has won!!!')
            return p

        if b['01'] == p and b['11'] == p and b['21'] == p:
            print('Player ' + p + ' has won!!!')
            return p
 
        if b['02'] == p and b['12'] == p and b['22'] == p:
            print('Player ' + p + ' has won!!!')
            return p
 
        # Diagonal lines
        if b['00'] == p and b['11'] == p and b['22'] == p:
            print('Player ' + p + ' has won!!!')
            return p

        if b['02'] == p and b['11'] == p and b['20'] == p:
            print('Player ' + p + ' has won!!!')
            return p


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

    cells = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
    # for cell in cells:
    #     play(board, 'x', cell)

    #game start

    p= 'x' 

    while True:

        draw_board(board)

        #invalid/valid plays
        while True:

            print('player ' + p + ' make a play')
            cell= input()

            if play(board, p , cell):
                break


        #check if we have winner
        if have_winner(board):
            break
    
        if is_full(board):
            print('game tied')
            break

        # flip flop variable
        if p =='x':
            p='o'
        else:
            p='x'



    draw_board(board)
    

if __name__ == "__main__":
    main()