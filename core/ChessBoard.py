import chess


# TODO Get Board
# TODO Get Possible Moves
# TODO check getters and setters

# all of it particular to the board in the current object

class ChessBoard:
    def __init__(self, fen: ''):
        self.board = chess.Board(fen)

    def isLegalMove(self, move):
        return move in self.board.legal_moves

    def isCheck(self):
        return self.board.is_check()

    def isCheckMate(self):
        return self.board.is_checkmate()

    def isStaleMate(self):
        return self.board.is_stalemate()

    def possibleMoves(self, alg_notation):
        arr = list(self.board.generate_legal_moves(from_mask=chess.parse_square(alg_notation)))
        print(arr)
