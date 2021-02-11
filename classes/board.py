import pygame
from .pieces import Pawn
class Board:
    def __init__(self, player1, player2):
        self.board = [[0 for x in range(8)] for _ in range(8)]
        self.turn = ""
        self.player1 = player1
        self.player2 = player2
        self.board[1][0] = Pawn(1, 0, "w")
        self.board[1][1] = Pawn(1, 1, "w")
        self.board[1][2] = Pawn(1, 2, "w")
        self.board[1][3] = Pawn(1, 3, "w")
        self.board[1][4] = Pawn(1, 4, "w")
        self.board[1][5] = Pawn(1, 5, "w")
        self.board[1][6] = Pawn(1, 6, "w")
        self.board[1][7] = Pawn(1, 7, "w")
        self.pos_pawn = (0,0)
    def draw(self, screen, color):
        self.board[0][0].draw(screen, "w")
    
    def move_piece(self):
        pass