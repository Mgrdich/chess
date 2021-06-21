from core.ChessUtil import ChessUtil


def Dec_isAlgebraicNotation(function):
    def wrapper(*args):
        alg_notation = args[1]
        if not ChessUtil.isAlgebraicNotation(alg_notation):
            raise Exception('Not valid Algebraic notation')

        func = function(*args)
        return func

    return wrapper
