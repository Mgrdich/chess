from Util.Lib import Lib
from core.ChessUtil import ChessUtil

"""
 Single field validation class 
 example Query params
"""

ERROR_KEYS = {
    'not_valid_key': 'Not a valid key',
    'not_valid_move_not':'Not a valid move notation',
    'is_required': 'This Field is required'
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
        if not item:
            obj = ErrorUtil.errorObj(name=name, msg=ERROR_KEYS['is_required'])
            return ErrorUtil.isInvalid(obj)

        return ErrorUtil.isValid()

    @staticmethod
    def isAlgNotation(name: str, alg_not: str):
        if not ChessUtil.isAlgebraicNotation(alg_not):
            obj = ErrorUtil.errorObj(name=name, msg=ERROR_KEYS['not_valid_key'])
            return ErrorUtil.isInvalid(obj)

        return ErrorUtil.isValid()

    @staticmethod
    def isValidMoveNotation(move_str: str):
        pass

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
