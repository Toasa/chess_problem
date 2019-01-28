import chess.pgn

pgn = open("./data/auerswald.pgn")

count = 1
while 1:
    game = chess.pgn.read_game(pgn)

    if game is None:
        break

    board = game.board()
    print("first board")
    print(board)
    input()

    for move in game.mainline_moves():
        board.push(move)
        print(move, count)
        print(board)
        input()
        count += 1

    print("end\n")
    count = 1
