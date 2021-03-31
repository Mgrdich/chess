import chess


# TODO Get Board
# TODO Get Possible Moves
# TODO check getters and setters

# all of it particular to the board in the current object

class ChessBoard:
    def __init__(self, fen=''):
        if fen:
            self.board = chess.Board(fen)
        else:
            self.board = chess.Board()

    def isLegalMove(self, move) -> bool:
        return move in self.getLegalMoves()

    def getLegalMoves(self):
        return self.board.legal_moves

    def isCheck(self) -> bool:
        return self.board.is_check()

    def isCheckMate(self) -> bool:
        return self.board.is_checkmate()

    def isStaleMate(self) -> bool:
        return self.board.is_stalemate()

    def printBoard(self):
        print(self.board)

    def possibleMoves(self, alg_notation: str) -> list:
        return list(self.board.generate_legal_moves(from_mask=ChessBoard.getBitSquare(alg_notation)))

    @staticmethod
    def getBitSquare(alg_notation):
        return chess.BB_SQUARES[chess.parse_square(alg_notation)]
