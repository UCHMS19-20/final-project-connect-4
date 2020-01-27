import numpy as np
import pygame
import sys
import math

#colors for the pieces and board
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

#the amount of ros and columns in a standard connect 4 board
ROW_COUNT = 6
COLUMN_COUNT = 7

#the command line connect 4
def create_board():
	board = np.zeros((ROW_COUNT,COLUMN_COUNT))
	return board

#makes it so the piece shows up
def drop_piece(board, row, col, piece):
	board[row][col] = piece

#defines which places pieces are allowed to be placed
def is_valid_location(board, col):
	return board[ROW_COUNT-1][col] == 0

#checks which row is open for a piece to be put in
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

#the board needs its axis to be flipped bc numpy starts at the top right
def print_board(board):
	print(np.flip(board, 0)) 

#checks if a player has won
def winning_move(board, piece):
	#check all horizontal locations for win
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True

#check all vertical locations for win
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True
	#check all positively sloped diagonals
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT-3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

	#check all negatively sloped diagonals
	for c in range(COLUMN_COUNT-3):
		for r in range(3, ROW_COUNT):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True

#draws the board with a blue rectangle with black circles over it to represent open spaces
def draw_board(board):
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):		
			if board[r][c] == 1:
				pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
			elif board[r][c] == 2: 
				pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
	pygame.display.update()


board = create_board()
print_board(board)
game_over = False
turn = 0

pygame.init()

SQUARESIZE = 50

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)

#so the circles aren’t touching
RADIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 37)

#actual game
while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		
		#moves the piece along with the mouse
		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
			posx = event.pos[0]
			if turn == 0:
				pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
			else:
				pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
		pygame.display.update()

		#if mouse is clicked, the piece is placed
		if event.type ==pygame.MOUSEBUTTONDOWN:
			#gets rid of the piece at the top after someone had won
			pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
		
			#ask player 1 input
			if turn == 0:
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))

				if is_valid_location(board, col):
					row = get_next_open_row(board, col)
					drop_piece(board, row, col, 1)
			
					if winning_move(board, 1):
						label = myfont.render("Player 1 wins!", 1, RED)
						screen.blit(label, (40,10))
						game_over = True
				
			#ask player 2 input
			else:
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))

				if is_valid_location(board, col):
					row = get_next_open_row(board, col)
					drop_piece(board, row, col, 2)

					if winning_move(board, 2):
						label = myfont.render("Player 2 wins!", 1, YELLOW)
						#blit is used to render the objects
						screen.blit(label, (40,10))
						game_over = True

			print_board(board)
			draw_board(board)
			turn += 1
			turn = turn % 2
			#waits three seconds after someone wins until window is exited out of
			if game_over:
				pygame.time.wait(5000)