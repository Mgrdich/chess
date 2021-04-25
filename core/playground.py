from core.ChessCore import ChessCore

core = ChessCore('r1bqkbnr/pppp1ppp/2n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq')

core.printBoard()
core.board.parse_san("Kg1")
#
print('--------')
core.printBoard()

print(core.board.piece_map())
