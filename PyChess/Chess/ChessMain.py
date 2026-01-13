"""
Main driver file. Responsible for handling user input and displaying the game.
"""
import pygame as p
from Chess import ChessEngine

WIDTH = 512
HEIGHT = 512
DIMENSION = 8
SQUARE_SIZE = HEIGHT / DIMENSION
MAX_FPS = 15
IMAGES = {}


# Init images only ones for optimal runtime. If we init images on every turn the program will be very loaded
# Note: images loaded to be the same as the SQUARE SIZE, but can be made smaller
def load_images():
    pieces = ["bR", "bN", "bB", "bQ", "bK", "bp", "wp", "wR", "wN", "wB", "wQ", "wK"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("ChessImages/" + piece + ".png"), (SQUARE_SIZE, SQUARE_SIZE))


# Main for the code. Will handle all input and update the game
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    load_images()  # load only once before the game loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

        draw_game_state(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()  # take everything done in the last frame and show it on screen


# Responsible for drawing the board and the pieces in it after every player turn
# We draw the board first, to be able to see the pieces on the board
def draw_game_state(screen, gs):
    draw_board(screen)
    draw_pieces(screen, gs.board)


# White has always even coords sum (0,0) = 0 -> white
# Black has always odd coords sum (0,1) = 1 -> black
def draw_board(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r + c) % 2]
            # Draw a rectangle on the screen, with the correct coordinates and the width and height
            p.draw.rect(screen, color, p.Rect(c*SQUARE_SIZE, r*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def draw_pieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":  # empty square
                screen.blit(IMAGES[piece], (c*SQUARE_SIZE, r*SQUARE_SIZE))


# Only run main if we run this file directly, not if we imported ChessMain.py
if __name__ == "__main__":
    main()




















