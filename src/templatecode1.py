import pygame
import sys

width, height = 600, 600
cell_count = 7
cell_size = width/cell_count

grid = []

class Cell:

    def __init__(self, x, y, sz):
        self.x = x
        self.y = y
        self.sz = sz
        self.filled = False
    
    def show(self):
        pygame.draw.rect(screen, pygame.Color("blue"), (self.x * self.sz,self.y * self.sz,self.sz,self.sz), 2)
        if self.filled:
            pygame.draw.rect(screen, pygame.Color("red"), (self.x * self.sz, self.y * self.sz, self.sz, self.sz))

pygame.init()

screen = pygame.display.set_mode((width, height))

for y in range(cell_count):
    for x in range(cell_count):
        grid.append(Cell(x, y, cell_size))

grid[3].filled = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    # pygame.draw.rect(screen, pygame.Color("red"), (0,0,50,50))
    for cell in grid:
        cell.show()
        
        
    pygame.display.flip()

#make a function for yellow and blue
#make a button for each space
#assign a color to a person and signify whos turn it is by using 0 or 1