import chess

board = chess.Board()

print(board)

board.push_san("e4")
print('-----')
print(board)
print(board.legal_moves)
print('-----')

board.push_san("Nh6")
print(board)
board.pop()
print('-----')
print(board)

board.generate_legal_moves()

