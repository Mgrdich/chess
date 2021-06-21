from core.ChessUtil import ChessUtil


def Dec_isAlgebraicNotation(is_method: bool):
    def decorator(function):
        def wrapper(*args):
            if is_method:
                alg_notation = args[1]
            else:
                alg_notation = args[0]

            if not ChessUtil.isAlgebraicNotation(alg_notation):
                raise Exception('Not valid Algebraic notation')

            return function(*args)

        return wrapper

    return decorator
