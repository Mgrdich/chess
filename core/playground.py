from core.ChessCore import ChessCore
import chess

# core = ChessCore('r1bqkbnr/pppp1ppp/2n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq') # castling
# # core = ChessCore()
# core.printBoard()
#
# move = core.board.push_san("0-0")
# print(chess.square_name(move.to_square))
#
# print(core.board.is_kingside_castling(move))
# print(core.board.is_castling(move))
# print(core.board.is_queenside_castling(move))
#
# print(type(move))
# #
# print('--------')
# core.printBoard()
#
# print(chess.PIECE_SYMBOLS[chess.PAWN])

# core1 = ChessCore('rnbqkbnr/pppppp1p/8/8/6pP/5PP1/PPPPP3/RNBQKBNR b KQkq h3 0 3')  # en passant
core1 = ChessCore('rnbqkbnr/pppppp2/8/7p/6PP/6P1/PPPPP3/RNBQKBNR b KQkq - 0 4')  # en passant
core1.printBoard()
print(core1.board.has_legal_en_passant())
# is_en_passant


core1.getPossibleMoves('esh')
