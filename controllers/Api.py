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

        core.printBoard()
        if ChessCore.isKing(element):
            composite_move = element.upper() + pos
            print(composite_move)
            # TODO check the castling and return that shit
            print(core.board.fen())
            print('Turn', core.getTurn())
            print('pos', pos)
            print('c', core.board.has_castling_rights(color=core.getTurn()))
            print('c1', core.board.has_kingside_castling_rights(color=core.getTurn()))
            print('c2', core.board.has_queenside_castling_rights(color=core.getTurn()))

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

        move_validation = ErrorUtil.isValidMoveNotation('move', data['move'])

        if not move_validation['valid']:
            return move_validation['response']

        session_key = BoardSessions.getBoardSession(request.referrer)

        core = ChessCore.getBoard(session_key)

        parsed_move_validation = ErrorUtil.isValidMove(core.board, 'move', data['move'])

        if not parsed_move_validation['valid']:
            return parsed_move_validation['response']

        core.movePiece(data['move'], session_key=session_key)

        core.printBoard()

        res = {
            'status': 1,
            'data': data
        }
        return Lib.resJson(res)
