import pygame
from .player import Player
from constants import WIDTH, HEIGHT
import os
from .board import Board
class Game:
    def __init__(self, screen):
        self.screen = screen
        player1 = Player("Dagner", "123", "asd@gmail.com")
        player2 = Player("Ronaldo", "321", "dsa@gmail.com")
        self.board = Board(player1, player2)
        
         #chessbg = pygame.image.load(os.path.join("img", "chessbg.png"))
    def update(self):
        board_img = pygame.transform.scale(pygame.image.load(os.path.join("assets","board.png")), (WIDTH, HEIGHT))
        self.screen.blit(board_img, (0, 0))
        self.board.draw(self.screen, "w")
        pygame.display.update()