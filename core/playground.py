from core.ChessCore import ChessCore
import chess

core = ChessCore('r1bqkbnr/pppp1ppp/2n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq')
# core = ChessCore()
core.printBoard()

move = core.board.push_san("0-0")
print(chess.square_name(move.to_square))

print(core.board.is_kingside_castling(move))
print(core.board.is_castling(move))
print(core.board.is_queenside_castling(move))

print(type(move))
#
print('--------')
core.printBoard()

print(chess.PIECE_SYMBOLS[chess.PAWN])
