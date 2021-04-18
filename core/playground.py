import chess

board = chess.Board()

print(board)

board.push_san("e4")
print('-----')
print(board)
print('-----')

board.push_san("Nh6")
print(board)

board.push_san("Nh3")
print(board)

