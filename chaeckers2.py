import pygame

pygame.init()
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

# RGB Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)

def draw_squares(win):
    win.fill(BLACK) # Start by making the whole background dark
    for row in range(ROWS):
        # This math ensures the colors alternate every row and column
        for col in range(row % 2, COLS, 2):
            pygame.draw.rect(win, WHITE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Draw the board
        draw_squares(WIN)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()