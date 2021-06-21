import numpy as np
from flask import session
import chess

from Util.BoardSessions import BoardSessions
from Util.Route import Routes
from core.ChessUtil import ChessUtil
from decorators.validation import Dec_isAlgebraicNotation


class ChessCore(ChessUtil):
    PIECE_SYMBOLS = chess.PIECE_SYMBOLS[1:]  # remove None
    BLACK_PIECE_SYMBOLS = PIECE_SYMBOLS  # lower case
    WHITE_PIECE_SYMBOLS = [i.upper() for i in BLACK_PIECE_SYMBOLS]  # upper case

    CASTLE_MOVE_POSITION = ['Ke1', 'Ke8']  # initial king position for pseudo checking :)

    CASTLING_ROOK_POSITION_WHITE = {  # TODO front api replace later
        'king': 'h1-f1',
        'queen': 'a1-c1'
    }

    CASTLING_ROOK_POSITION_BLACK = {
        'king': 'h8-f8',
        'queen': 'a8-c8'
    }

    KING_SIDE_CASTLE = '0-0'
    QUEEN_SIDE_CASTLE = '0-0-0'

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

    def getTurn(self) -> chess.Color:  # TODO convert me to getter
        return self.board.turn

    def setBoardToSession(self, session_key: str = DEFAULT_GAME_SESSION):
        session[session_key] = self.board.fen()

    def printBoard(self):
        print(self.board)

    def movePiece(self, move_notation: str, session_key: str) -> chess.Move:
        move = self.movePieceSan(move_notation)
        self.setBoardToSession(session_key)
        return move

    def movePieceSan(self, move_notation: str) -> chess.Move:
        return self.board.push_san(move_notation)

    def getCastlingMove(self, move: chess.Move, color: chess.Color) -> object:
        obj = {}
        if not self.board.is_castling(move):
            obj['castling'] = False
            return obj

        obj['castling'] = True

        if color == chess.WHITE:
            rookConfig = ChessCore.CASTLING_ROOK_POSITION_WHITE
        else:
            rookConfig = ChessCore.CASTLING_ROOK_POSITION_BLACK

        if self.board.is_kingside_castling(move):
            obj['castlingMove'] = rookConfig['king']
            return obj

        obj['castlingMove'] = rookConfig['queen']
        return obj

    @Dec_isAlgebraicNotation(is_method=True)
    def getPossibleMoves(self, alg_notation: str) -> np.ndarray:
        return np.array(
            list(self.board.generate_legal_moves(from_mask=ChessCore.getBitSquare(alg_notation)))
        )

    @Dec_isAlgebraicNotation(is_method=True)
    def getPossibleMovesAlg(self, alg_notation: str) -> object:
        moves = self.getPossibleMoves(alg_notation)

        # TODO fix me with np.fromiter or something to fix this generator issue
        # i think the issue is something with
        # ValueError: Must specify length when using variable-size data-type.
        return {
            'result': np.array(list(map(lambda move: chess.square_name(move.to_square), moves))),
            'moves': moves
        }

    @staticmethod
    @Dec_isAlgebraicNotation(is_method=False)
    def getBitSquare(alg_notation: str):
        return chess.BB_SQUARES[chess.parse_square(alg_notation)]

    # TODO check whether is okay to be here or in an individual function
    @staticmethod
    def getBoard(session_key: str = DEFAULT_GAME_SESSION):
        if session_key in session:
            return ChessCore(session[session_key])

        raise Exception('Something Wrong with the Board Session')
