import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    global ROW_COUNT,COLUMN_COUNT
    return np.zeros((ROW_COUNT, COLUMN_COUNT))

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board,0))

def winning_move(board, piece):
    #check all horizontal locations
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    #check for all vertical locations
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    #check positive slope
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    #check negative slope
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c-1] == piece and board[r-2][c-2] == piece and board[r-3][c-3] == piece:
                return True

board = create_board()
print_board(board)

game_over = False
turn = 0

while not game_over:
    #Ask player 1 input
    if turn == 0:
        col = int(input("Player 1 Selection(0-6):"))
        if col < COLUMN_COUNT and is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)
        else: continue

        if winning_move(board, 1):
            print("\n\nPlayer 1 Wins!!! Congrats!!!\n")
            game_over = True
    #Ask Player 2 input
    else:
        col = int(input("Player 2 Selection(0-6):"))
        if col < COLUMN_COUNT and is_valid_location(board, col) and col < COLUMN_COUNT:
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
        else: continue

        if winning_move(board, 2):
            print("\n\nPlayer 2 Wins!!! Congrats!!!\n")
            game_over = True

    print_board(board)

    turn += 1
    turn = turn % 2

