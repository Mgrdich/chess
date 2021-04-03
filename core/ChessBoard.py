import chess
import numpy as np

# TODO Create Algebraic notation hash for validation in this class or seperate them


class ChessCore:
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

    def getPossibleMoves(self, alg_notation: str) -> np.ndarray[chess.Move]:
        return np.array(self.board.generate_legal_moves(from_mask=ChessCore.getBitSquare(alg_notation)))

    def getPossibleMovesAlg(self, alg_notation: str) -> np.ndarray[str]:
        moves = self.getPossibleMoves(alg_notation)
        return np.array(map(lambda move: chess.square_name(move.to_square), moves))

    @staticmethod
    def getBitSquare(alg_notation):
        return chess.BB_SQUARES[chess.parse_square(alg_notation)]
