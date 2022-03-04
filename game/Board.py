import pygame
from enum import Enum

SIZE = [800, 500]
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

class squr(Enum):
    EMPTY = 1
    FOOD = 2
    HEAD = 3
    BODY = 4

class board:
    SQUR_SIZE = 50
    BOARD_LENGTH = 10
    board = [[]]
    screen = None
    clock = None

    #initialize the board, create the screen and dispaly the screen.
    def __init__(self):
        pygame.init()
        SIZE = [self.BOARD_LENGTH * self.SQUR_SIZE, 
                self.BOARD_LENGTH * self.SQUR_SIZE]

        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption("snake")
        
        self.screen.fill(WHITE)

        for i in range(self.BOARD_LENGTH):
            for j in range (self.BOARD_LENGTH):
                self.board[i].append(squr.EMPTY)
            self.board.append([])

        self.receate_screen()

        pygame.display.flip()

    # draw the squres on the screen by the list 'bosrd'
    def receate_screen(self):
        is_white = True
        for row in range(self.BOARD_LENGTH):
            if (self.BOARD_LENGTH%2 == 0):
                is_white = not is_white
            for col in range(self.BOARD_LENGTH):
                SIZE = (col * self.SQUR_SIZE, row * self.SQUR_SIZE, self.SQUR_SIZE, self.SQUR_SIZE)
                match (self.board[row][col]):
                    case squr.HEAD:
                        pygame.draw.rect(self.screen, BLACK, SIZE)
                    case squr.BODY:
                        pygame.draw.rect(self.screen, BLUE, SIZE)
                    case squr.FOOD:
                        pygame.draw.rect(self.screen, RED, SIZE)
                    case squr.EMPTY:
                        if (is_white):
                            pygame.draw.rect(self.screen, GREEN, SIZE)
                            is_white = False
                        else:
                            pygame.draw.rect(self.screen, WHITE, SIZE)
                            is_white = True

    # get a list of changes update the screen and difplay it
    # change format: [X_index, Y_index, new_state]
    # new_state = squr.HEAD / EMPTY / FOOD / BODY
    def update(self, changes):
        for change in changes:
            self.board[change[0]][change[1]] = change[2]

        self.receate_screen()

        pygame.display.flip()
