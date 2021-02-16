import pygame
import os
from constants import WIDTH, HEIGHT, BOARD_HEIGHT, BOARD_WIDTH, MARGIN_X, MARGIN_Y, SQUARE_SIE
w_pawn = pygame.image.load(os.path.join("assets", "white_pawn.png"))

w = [w_pawn]

W = []
for img in w:
    W.append(pygame.transform.scale(img, (BOARD_WIDTH//8, BOARD_HEIGHT//8)))

class Piece:
    rect = (MARGIN_X, MARGIN_Y, BOARD_WIDTH, BOARD_HEIGHT)
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.move_list = []
        #peon y rey ya que tienen comportamientos distintos a la de las otras piezas
        self.king = False
        self.pawn = False
    
    def draw(self, screen, color):
        drawThis = W[self.img]
        screen.blit(drawThis, (MARGIN_X + SQUARE_SIE * self.col, MARGIN_Y + SQUARE_SIE * self.row))

class Pawn(Piece):
    img = 0
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.pawn = True



