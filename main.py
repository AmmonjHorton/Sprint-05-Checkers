import pygame
from chaeckers2 import draw_squares, WIN, ROWS, COLS, SQUARE_SIZE, RED, GREY, WHITE
import board
def main():
    run = True
    clock = pygame.time.Clock()
    board = board.Board() # Create our board instance

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Draw everything
        board.draw(WIN)
        pygame.display.update()

    pygame.quit()