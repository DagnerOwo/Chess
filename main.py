import pygame
from classes.game import Game
from constants import BLACK, BLUE, WHITE, WIDTH, HEIGHT

pygame.init()
screen=pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Chess')
def main():
    game = Game(screen)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                game.board.move_piece()

        game.update()
main()