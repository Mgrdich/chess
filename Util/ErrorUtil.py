import chess

from Util.Lib import Lib
from core.ChessCore import ChessCore
from core.ChessUtil import ChessUtil

"""
 Single field validation class 
 example Query params
"""

ERROR_KEYS = {
    'not_valid_key': 'Not a valid key',
    'not_valid_move_not': 'Not a valid move notation',
    'is_required': 'This Field is required',
    'not_valid_possible_move': 'Not a valid Possible Move'
}


class ErrorUtil:

    def __init__(self):
        pass

    @staticmethod
    def errorObj(name: str, msg: str) -> object:
        return {
            'status': 0,
            'errors': {
                name: msg
            }
        }

    # maybe add any number of required parameters
    @staticmethod
    def isRequired(name: str, item):
        if name not in item:
            obj = ErrorUtil.errorObj(name=name, msg=ERROR_KEYS['is_required'])
            return ErrorUtil.isInvalid(obj)

        return ErrorUtil.isValid()

    @staticmethod
    def isAlgNotation(name: str, alg_not: str) -> object:
        if not ChessUtil.isAlgebraicNotation(alg_not):
            obj = ErrorUtil.errorObj(name=name, msg=ERROR_KEYS['not_valid_key'])
            return ErrorUtil.isInvalid(obj)

        return ErrorUtil.isValid()

    @staticmethod
    def isValidMoveNotation(name: str, move_str: str) -> object:
        if len(move_str) != 3 and len(move_str) != 2:
            obj = ErrorUtil.errorObj(name=name, msg=ERROR_KEYS['not_valid_move_not'])
            return ErrorUtil.isInvalid(obj)

        if len(move_str) == 2:
            if move_str[0] not in chess.FILE_NAMES or move_str[1] not in chess.RANK_NAMES:
                obj = ErrorUtil.errorObj(name=name, msg=ERROR_KEYS['not_valid_move_not'])
                return ErrorUtil.isInvalid(obj)
            else:
                return ErrorUtil.isValid()

        # len 3
        if move_str[0].lower() not in ChessCore.PIECE_SYMBOLS or move_str[1] not in chess.FILE_NAMES \
                or move_str[2] not in chess.RANK_NAMES:
            obj = ErrorUtil.errorObj(name=name, msg=ERROR_KEYS['not_valid_move_not'])
            return ErrorUtil.isInvalid(obj)

        return ErrorUtil.isValid()

    @staticmethod
    def isValidMove(c: chess.Board, name: str, move_str: str) -> object:
        try:
            c.parse_san(move_str)
            return ErrorUtil.isValid()
        except ValueError:
            obj = ErrorUtil.errorObj(name=name, msg=ERROR_KEYS['not_valid_possible_move'])
            return ErrorUtil.isInvalid(obj)

    @staticmethod
    def isValid() -> object:
        return {
            'valid': True,
            'response': None
        }

    @staticmethod
    def isInvalid(res: object) -> object:
        return {
            'valid': False,
            'response': Lib.resJson(res)
        }
