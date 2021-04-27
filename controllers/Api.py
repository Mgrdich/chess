import chess
from flask import request
from flask.views import MethodView

from Util.BoardSessions import BoardSessions
from Util.Lib import Lib
from Util.ErrorUtil import ErrorUtil
from core.ChessCore import ChessCore


# Possible Move
class MovesApi(MethodView):
    """ api/moves?pos=e3&elem=k"""

    @staticmethod
    def get():
        """ Return the entire inventory collection """
        pos = request.args.get('pos')

        element = request.args.get('elem')

        pos_required = ErrorUtil.isRequired('pos', pos)

        if not pos_required['valid']:
            return pos_required['response']

        element_required = ErrorUtil.isRequired('element', element)

        if not element_required['valid']:
            return element_required['response']

        pos_validation = ErrorUtil.isAlgNotation('pos', pos)

        if not pos_validation['valid']:
            return pos_validation['response']

        session_key = BoardSessions.getBoardSession(request.referrer)

        # Board

        core = ChessCore.getBoard(session_key)

        res = {
            'status': 1,
            'result': core.getPossibleMovesAlg(pos).tolist()
        }

        # core.printBoard()

        composite_move = element.upper() + pos
        c = ChessCore.CASTLE_MOVE_POSITION

        if ChessCore.isKing(element) and composite_move in c and core.board.has_castling_rights(color=core.getTurn()):
            castlingMoves = []

            if core.board.has_kingside_castling_rights(color=core.getTurn()):
                try:
                    kMove = core.board.parse_san(ChessCore.KING_SIDE_CASTLE)
                    castlingMoves.append(chess.square_name(kMove.to_square))  # TODO move to our api with a function
                except ValueError:
                    pass

            if core.board.has_queenside_castling_rights(color=core.getTurn()):
                try:
                    qMove = core.board.parse_san(ChessCore.QUEEN_SIDE_CASTLE)
                    castlingMoves.append(chess.square_name(qMove.to_square))  # TODO move to our api with a function
                except ValueError:
                    pass

            if len(castlingMoves) > 0:
                res['castling'] = castlingMoves

        return Lib.resJson(res)


# Moves
class MakeMoveApi(MethodView):
    """ api/make-move """

    @staticmethod
    def post():
        """ Sets chess play in the Core """
        data = request.get_json()

        required_validation = ErrorUtil.isRequired('move', data['move'])

        if not required_validation['valid']:
            return required_validation['response']

        session_key = BoardSessions.getBoardSession(request.referrer)

        core = ChessCore.getBoard(session_key)

        try:
            move = core.movePiece(data['move'], session_key=session_key)
            # print(move.to_square)
        except ValueError:
            return Lib.resInvalidJson('invalid Move')

        core.printBoard()

        res = {
            'status': 1,
            'data': move.to_square
        }
        return Lib.resJson(res)
