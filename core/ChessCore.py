import numpy as np
from flask import session
import chess

from Util.BoardSessions import BoardSessions
from Util.Route import Routes
from core.ChessUtil import ChessUtil


class ChessCore(ChessUtil):
    PIECE_SYMBOLS = chess.PIECE_SYMBOLS[1:]  # remove None
    BLACK_PIECE_SYMBOLS = PIECE_SYMBOLS  # lower case
    WHITE_PIECE_SYMBOLS = [i.upper() for i in BLACK_PIECE_SYMBOLS]  # upper case

    whiteKingSideCastle = 'Kg1'
    whiteQueenSideCastle = 'Kf1'
    blackKingSideCastle = 'Kg8'
    blackQueenSideCastle = 'Kf8'

    whiteKingInitial = 'Ke1'
    blackKingInitial = 'Ke8'

    castling = {
        whiteKingSideCastle: '0-0',
        whiteQueenSideCastle: '0-0-0',
        blackKingSideCastle: '0-0',
        blackQueenSideCastle: '0-0-0'
    }

    castlingPositions = {
        whiteKingInitial: {
            'kingSide': 'g1',
            'queenSide': 'b1'
        },
        blackKingInitial: {
            'kingSide': 'g8',
            'queenSide': 'b8'
        }
    }

    DEFAULT_GAME_SESSION = BoardSessions.getBoardSession(Routes.Game_Url)

    def __init__(self, fen: str = ''):
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

    def getTurn(self):  # TODO convert me to getter
        return self.board.turn

    def setBoardToSession(self, session_key: str = DEFAULT_GAME_SESSION):
        session[session_key] = self.board.fen()

    def printBoard(self):
        print(self.board)

    def movePiece(self, move_notation: str, session_key: str):
        self.movePieceSan(move_notation)
        self.setBoardToSession(session_key)

    def movePieceSan(self, move_notation: str):
        self.board.push_san(move_notation)

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
    def getBitSquare(alg_notation: str):
        if not ChessUtil.isAlgebraicNotation(alg_notation):
            raise Exception('Not valid Algebraic notation')

        return chess.BB_SQUARES[chess.parse_square(alg_notation)]

    # TODO check whether is okay to be here or in an individual function
    @staticmethod
    def getBoard(session_key: str = DEFAULT_GAME_SESSION):
        if session_key in session:
            return ChessCore(session[session_key])

        raise Exception('Something Wrong with the Board Session')
