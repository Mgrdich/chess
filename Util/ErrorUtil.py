from Util.Util import Util
from core.ChessUtil import ChessUtil

"""
 Single field validation class 
 example Query params
"""


class ErrorUtil:
    errors_keys = {
        'not_valid_key': 'Not a valid key',
        'is_required': 'This Field is required'
    }

    def __init__(self):
        pass

    # maybe add any number of required parameters
    def isRequired(self, name: str, item):
        if not item:
            obj = {
                'status': 0,
                'errors': {
                    [name]: self.errors_keys['is_required']
                }
            }
            return ErrorUtil.isInvalid(obj)

        return ErrorUtil.isValid()

    def isAlgNotation(self, name: str, alg_not: str):
        if not ChessUtil.isAlgebraicNotation(alg_not):
            obj = {
                'status': 0,
                'errors': {
                    [name]: self.errors_keys['not_valid_key']
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
            'response': Util.resJson(res),
        }
