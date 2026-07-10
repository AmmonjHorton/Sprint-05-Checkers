import pygame
from piece import Piece
from chaeckers2 import draw_squares, WIN, ROWS, COLS, SQUARE_SIZE, RED, GREY, WHITE
class Board:
    def __init__(self):
        self.board = []
        self.create_board()

    def create_board(self):
        """Initializes the 2D array and populates it with Piece objects."""
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                # Pieces only go on dark squares
                if col % 2 == (row + 1) % 2:
                    if row < 3:
                        self.board[row].append(Piece(row, col, RED))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, GREY))
                    else:
                        self.board[row].append(0) # 0 means empty square
                else:
                    self.board[row].append(0)

    def draw(self, win):
        """Draws the squares first, then loops through the grid to draw pieces."""
        draw_squares(win) # Uses the function we made in Step 2
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)