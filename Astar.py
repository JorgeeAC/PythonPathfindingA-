import pygame
import math
from queue import PriorityQueue

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,255,0)
YELLOW = (255,255,0)
WHITE= (255,255,255)
BLACK= (0,0,0)
PURPLE = (128,0,128)
ORANGE = (255,165,0)
GREY= (128,128,128)
TURQUOISE = (64,244,208)

class Node:
    def __init__(self,row,col,width,total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    #These methods are following the process of checking
    # the color of the node to see it's condition
    #Red - Closed, Black - Border etc
    def getPos(self):
        return self.row, self.col

    def isClosed(self):
        return self.color == RED
    def isOpen(self):
        return self.color == GREEN

    def isBarrier(self):
        return self.color == BLACK

    def isStart(self):
        return self.color == ORANGE
    def isEnd(self):
        return self.color == TURQUOISE
    def reset(self):
        return self.color == WHITE

    #These methods will make the nodes the colors you want 
    # it to be 
    def makeClosed(self):
        self.color = RED
    
    def makeStart(self):
        self.color = ORANGE

    def makeOpen(self):
        self.color = GREEN
    def makeBarrier(self):
        self.color = BLACK
    def makeEnd(self):
        self.color = TURQUOISE
    def makePath(self):
        self.color = PURPLE
    def draw(self,win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.width))

    def updateNeighbors(self, grid):
        pass
    def __lt__(self,other):
        return False

    #end Class

# Guess Distance, manhatten distance
#
def h(p1,p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1-y2)

#Create the grid 
def makeGrid(rows,width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j , gap, rows)
            grid[i].append(node)
    return grid

def drawGrid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0,i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap,0), (j * gap,width))

def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(win)

    drawGrid(win, rows, width)
    pygame.display.update()

def getClickedPos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap
    
    return row, col



def main (win, width):
    ROWS = 50
    grid = makeGrid(ROWS, width)

    start = None
    end = None

    run = True
    started = False

    while run:
        draw(win,grid,ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                continue
            
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row , col = getClickedPos(pos,ROWS,width)
                node = grid[row][col]
                if not start:
                    start = node
                    start.makeStart()

                elif not end:
                    end = node
                    end.makeEnd()
                
                elif node != end and node != start: 
                    node.makeBarrier()


            elif pygame.mouse.get_pressed()[2]:
                pass

    pygame.quit()

main(WIN, WIDTH)





    



        


