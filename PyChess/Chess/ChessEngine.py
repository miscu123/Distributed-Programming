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

    def make_move(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)  # log the move if we want to undo
        self.whiteToMove = not self.whiteToMove  # end player turn

    def undo_move(self):
        if len(self.moveLog) > 0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove

# We need to make sure that when we make a move, the king is not in check, therefore we first need to check all the
# possible moves before te valid ones. If a king is in check, we can not move
    def get_valid_moves(self):
        return self.get_all_possible_moves()  # dont worry about check for now

    def get_all_possible_moves(self):
        moves = []
        for r in range(len(self.board)):  # rows
            for c in range(len(self.board[r])):  # cols in a row
                turn = self.board[r][c][0]  # [0] means we either get 'b' or 'w'
                if (turn == 'w' and self.whiteToMove) and (turn == 'b' and not self.whiteToMove):
                    piece = self.board[r][c][1]  # [1] means we get the piece type
                    if piece == 'p':
                        self.get_pawn_moves(r, c, moves)
                    elif piece == 'R':
                        self.get_rook_moves(r, c, moves)
                    elif piece == 'N':
                        self.get_knight_moves(r, c, moves)
                    elif piece == 'B':
                        self.get_bishop_moves(r, c, moves)
                    elif piece == 'Q':
                        self.get_queen_moves(r, c, moves)
                    elif piece == 'K':
                        self.get_king_moves(r, c, moves)

        return moves

    def get_pawn_moves(self, r, c, moves):
        pass

    def get_rook_moves(self, r, c, moves):
        pass

    def get_knight_moves(self, r, c, moves):
        pass

    def get_bishop_moves(self, r, c, moves):
        pass

    def get_queen_moves(self, r, c, moves):
        pass

    def get_king_moves(self, r, c, moves):
        pass


# Move class to handle our move info like starting / ending positions, the captured piece, the moved piece...
class Move:
    # we make dictionaries for the ranks in chess, and we invert the dict
    # we want to make chess notations for the player move
    ranks_to_rows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rows_to_ranks = {v: k for k, v in ranks_to_rows.items()}

    files_to_cols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    cols_to_files = {v: k for k, v in files_to_cols.items()}

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        # creating a unique move ID for every move (maybe a bit overkill but is good practice to keep track)
        # for example 0004 would be a move from [0,0] to [0,4]
        self.move_id = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.move_id == other.move_id
        return False

    def get_chess_notation(self):
        return self.get_rank_file(self.startRow, self.startCol) + self.get_rank_file(self.endRow, self.endCol)

    # In chess notation you first need files and then ranks (A4, C1, B3..)
    def get_rank_file(self, r, c):
        return self.cols_to_files[c] + self.rows_to_ranks[r]








