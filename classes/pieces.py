import pygame
import os
from constants import WIDTH, HEIGHT
w_pawn = pygame.image.load(os.path.join("assets", "white_pawn.png"))

w = [w_pawn]

W = []
for img in w:
    W.append(pygame.transform.scale(img, (55, 55)))

class Piece:
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
        screen.blit(drawThis, (300 , 300))

class Pawn(Piece):
    img = 0
    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.pawn = True



