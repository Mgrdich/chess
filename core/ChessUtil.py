import chess


class ChessUtil:

    def __init__(self):
        pass

    @staticmethod
    def isAlgebraicNotation(alg_notation: str) -> bool:
        try:
            chess.parse_square(alg_notation)
        except ValueError:
            return False

        return True

    @staticmethod
    def isKing(notation: str) -> bool:
        return notation.lower() == 'k'
