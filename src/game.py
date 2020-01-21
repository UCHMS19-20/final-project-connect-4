Import numpy as np
Import pygame
Import sys
Import math

#colors for the pieces and board
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

#the amount of ros and columns in a standard connect 4 board
ROW_COUNT = 6
COLUMN_COUNT = 7

#the command line connect 4
Def create_board():
	Board = np.zeros((ROW_COUNT,COLUMN_COUNT))
	Return board

#makes it so the piece shows up
Def drop_piece(board, row, col, piece):
	Board[row][col] = piece

#defines which places pieces are allowed to be placed
Def is_valid_location(board, col):
	Return board[ROW_COUNT-1][col] == 0

#checks which row is open for a piece to be put in
Def get_next_open_row(board, col):
	For r in range(ROW_COUNT)
		If board[r][col] == 0:
			Return r
#the board needs its axis to be flipped bc numpy starts at the top right
Def print_board(board):
	print(np.flip(board, 0))

#checks if a player has won
Def winning_move(board, piece):
	#check all horizontal locations for win
	For c in range(COLUMN_COUNT-3):
		For r in range(ROW_COUNT):
			If board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				Return True

#check all vertical locations for win
	For c in range(COLUMN_COUNT):
		For r in range(ROW_COUNT-3):
			If board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				Return True
	#check all positively sloped diagonals
	For c in range(COLUMN_COUNT-3):
		For r in range(ROW_COUNT-3):
			If board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				Return True

	#check all negatively sloped diagonals
	For c in range(COLUMN_COUNT-3):
		For r in range(3, ROW_COUNT):
			If board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				Return True

#draws the board with a blue rectangle with black circles over it to represent open spaces
Def draw_board(board):
	For c in range(COLUMN_COUNT):
		For r in range(ROW_COUNT):
			pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	
	#shows that a slot is filled by putting a red or yellow place in the slot
For c in range(COLUMN_COUNT):
		For r in range(ROW_COUNT):	
	if board[r][c] == 1:
		pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
	Elif board[r][c] == 2: 
		pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)

	pygame.display.update()


Board = create_board()
print_board(board)
Game_over = False
Turn = 0

pygame.init()

SQUARESIZE = 100

Width = COLUMN_COUNT * SQUARESIZE
Height = (ROW_COUNT+1) * SQUARESIZE

Size = (width, height)

#so the circles aren’t touching
RADIUS = int(SQUARESIZE/2 - 5)

Screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

Myfont = pygame.font.SysFont(“monospace”, 75)
#actual game
While not game_over:
	For event in pygame.event.get():
		If event.type == pygame.QUIT:
			sys.exit()
		
		#moves the piece along with the mouse
		If event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
			Posx = event.pos[0]
			If turn == 0:
				pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
			Else:
				pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
		pygame.display.update()

		#if mouse is clicked, the piece is placed
		If event.type ==pygame.MOUSEBUTTONDOWN:
			#gets rid of the piece at the top after someone had won
			pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
		
	#ask player 1 input
	If turn == 0:
		Posx = event.pos[0]
		col = int(math.floor(posx/SQUARESIZE))

		If is_valid_location(board, col):
			Row = get_next_open_row(board, col)
			drop_piece(board, row, col, 1)
	
			If winning_move(board, 1):
				Label = mfont.render(“Player 1 wins!”, 1, RED)
				screen.blit(label, (40,10))
				Game_over = True
		
	#ask player 2 input
	Else:
		Posx = event.pos[0]
		col = int(math.floor(posx/SQUARESIZE))

		If is_valid_location(board, col):
			Row = get_next_open_row(board, col)
			drop_piece(board, row, col, 2)

			If winning_move(board, 2):
				Label = mfont.render(“Player 1 wins!”, 1, YELLOW)
				screen.blit(label, (40,10))
				Game_over = True

print_board(board)
draw_board(board)
Turn += 1
Turn = turn % 2
#waits three seconds after someone wins until window is exited out of
If game_over:
	pygame.time.wait(3000)