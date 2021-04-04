from Util.Lib import Lib
from core.ChessUtil import ChessUtil

"""
 Single field validation class 
 example Query params
"""

ERROR_KEYS = {
    'not_valid_key': 'Not a valid key',
    'is_required': 'This Field is required'
}


class ErrorUtil:

    def __init__(self):
        pass

    # maybe add any number of required parameters
    @staticmethod
    def isRequired(name: str, item):
        if not item:
            obj = {
                'status': 0,
                'errors': {
                    name: ERROR_KEYS['is_required']
                }
            }
            return ErrorUtil.isInvalid(obj)

        return ErrorUtil.isValid()

    @staticmethod
    def isAlgNotation(name: str, alg_not: str):
        if not ChessUtil.isAlgebraicNotation(alg_not):
            obj = {
                'status': 0,
                'errors': {
                    name: ERROR_KEYS['not_valid_key']
                }
            }
            return ErrorUtil.isInvalid(obj)

        return ErrorUtil.isValid()

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
