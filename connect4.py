import numpy as np
import pygame
import sys, math

ROW_COUNT = 10
COLUMN_COUNT = 10

BLUE = (0,0,255)
BLACK = (0,0,0)
YELLOW = (255, 255, 0)
RED = (255,0, 0)
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

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK,(int(c*SQUARESIZE + SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS )

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED,(int(c*SQUARESIZE + SQUARESIZE/2), height - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS )
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW,(int(c*SQUARESIZE + SQUARESIZE/2), height - int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS )

    pygame.display.update()

def is_draw(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 0:
                return False
    else:
        return True

board = create_board()
game_over = False
turn = 0

pygame.init()

SQUARESIZE = 50 #100PX
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
RADIUS = int(SQUARESIZE / 2 - 5)

size = (width, height)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", int(0.65 * SQUARESIZE))

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            #Ask player 1 input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)
                else: continue

                if winning_move(board, 1):
                    if is_draw(board):
                        label = myfont.render("Draw!!!", 1, BLUE)
                    else:
                        label = myfont.render("Red Wins!!!", 1, RED)
                    screen.blit(label, (40, 10))
                    game_over = True
            #Ask Player 2 input
            elif turn == 1:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)
                else: continue

                if winning_move(board, 2):
                    if is_draw(board):
                        label = myfont.render("Draw!!!", 1, BLUE)
                    else:
                        label = myfont.render("Yellow Wins!!!", 1, YELLOW)
                    screen.blit(label, (40, 10))
                    game_over = True

            if not game_over and is_draw(board):
                    label = myfont.render("Draw!!!", 1, BLUE)
                    screen.blit(label, (40, 10))
                    game_over = True

            turn += 1
            turn = turn % 2 #flip turns

    # print_board(board)
    draw_board(board)

    if game_over:
        pygame.time.wait(3000)
        board = create_board()
        game_over = False

