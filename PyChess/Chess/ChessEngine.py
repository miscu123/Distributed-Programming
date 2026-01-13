"""
Responsible for storing info about the game and executing callbacks. It will handle game logic, valid moves, etc.
"""


class GameState:
    def __init__(self):
        # board is 8x8 2d list. 'b' means black & 'w' means white
        # 'N' == knight because 'king' already has K
        # '--' == empty space with no piece on it
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.whiteToMove = True
        self.moveLog = []