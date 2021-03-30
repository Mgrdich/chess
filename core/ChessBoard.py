import chess


# TODO Get Board
# TODO Get Possible Moves
# TODO is Checkmate
# TODO is Stalemate

# all of it particular to the board in the current object


class ChessBoard:
    def __init__(self, fen: ''):
        self.board = chess.Board(fen)
