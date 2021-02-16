import pygame
from classes.game import Game
from constants import BLACK, BLUE, WHITE, WIDTH, HEIGHT, BOARD_HEIGHT, BOARD_WIDTH, MARGIN_X, MARGIN_Y, SQUARE_SIE

pygame.init()
screen=pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Chess')
def get_row_col(x, y):
    if x <= MARGIN_X or x >= MARGIN_X + BOARD_WIDTH:
        print("FUERA EN X")
    elif y <= MARGIN_Y or y >= MARGIN_Y + BOARD_HEIGHT:
        print("FUERA EN Y")
    else:
        row = (y - MARGIN_Y) // SQUARE_SIE
        col = (x - MARGIN_X) // SQUARE_SIE
        print( row, col )
def main():
    game = Game(screen)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = get_row_col(x, y)
        game.update()
main()