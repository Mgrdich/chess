import numpy as np
from flask import session
import chess
from Util.Serialize import Serialize

from core.ChessUtil import ChessUtil


# TODO maybe there should be a start function to init the the chess thingy while the class
# Just creates the context

class ChessCore(ChessUtil):
    def __init__(self, fen=''):
        if fen:
            self.board = chess.Board(fen)
        else:
            self.board = chess.Board()

        super().__init__()

    def isLegalMove(self, move) -> bool:
        return move in self.getLegalMoves()

    def getLegalMoves(self) -> chess.LegalMoveGenerator:
        return self.board.legal_moves

    def isCheck(self) -> bool:
        return self.board.is_check()

    def isCheckMate(self) -> bool:
        return self.board.is_checkmate()

    def isStaleMate(self) -> bool:
        return self.board.is_stalemate()

    def setMyBoardSession(self):
        session['board'] = self.board.fen()

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

    # TODO refactor set and get into a different class with inheritance and stuff
    @staticmethod
    def getMyBoardSession():
        if 'board' in session:
            return ChessCore(session['board'])

        return ChessCore()
