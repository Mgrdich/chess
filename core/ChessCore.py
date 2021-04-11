import chess
import numpy as np
from flask import session

from core.ChessUtil import ChessUtil


class ChessCore(ChessUtil):
    def __init__(self, fen=''):
        if fen:
            self.board = chess.Board(fen)
        else:
            self.board = chess.Board()

        super().__init__()

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

    # TODO turn this validation to a decorator
    def getPossibleMoves(self, alg_notation: str) -> np.ndarray:
        if not ChessUtil.isAlgebraicNotation(alg_notation):
            raise Exception('Not valid Algebraic notation')

        return np.array(
            list(self.board.generate_legal_moves(from_mask=ChessCore.getBitSquare(alg_notation)))
        )

    def getPossibleMovesAlg(self, alg_notation: str) -> np.ndarray:
        if not ChessUtil.isAlgebraicNotation(alg_notation):
            raise Exception('Not valid Algebraic notation')

        moves = self.getPossibleMoves(alg_notation)

        # TODO fix me with np.fromiter or something to fix this generator issue
        # i think the issue is something with
        # ValueError: Must specify length when using variable-size data-type.
        return np.array(list(map(lambda move: chess.square_name(move.to_square), moves)))

    @staticmethod
    def getBitSquare(alg_notation):
        if not ChessUtil.isAlgebraicNotation(alg_notation):
            raise Exception('Not valid Algebraic notation')

        return chess.BB_SQUARES[chess.parse_square(alg_notation)]

    @staticmethod
    def getMyBoardSession():
        return session['board']

    @staticmethod
    def setMyBoardSession(fen: str):
        session['board'] = fen
