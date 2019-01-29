import chess.pgn
import chess

def get_value(board):
    # material advantage
    values = {chess.PAWN: 1,
              chess.KNIGHT: 3,
              chess.BISHOP: 3.3,
              chess.ROOK: 5,
              chess.QUEEN: 9,
              chess.KING: 0}

    val = 0.0
    # piece values
    pm = board.piece_map()
    for x in pm:
        tval = values[pm[x].piece_type]
        if pm[x].color == chess.WHITE:
            val += tval
        else:
            val -= tval

    # add a number of legal moves term
    bak = board.turn
    board.turn = chess.WHITE
    val += 0.1 * board.legal_moves.count()
    board.turn = chess.BLACK
    val -= 0.1 * board.legal_moves.count()
    board.turn = bak

    # val of center board

    # king position(defensive of kings)

    # available castling?

    # connected of pieces、紐チェック

    return val

def print_init_position():
    print("a b c d e f g h ")
    print("                8")
    print("                7")
    print("                6")
    print("                5")
    print("                4")
    print("                3")
    print("                2")
    print("                1")

def main():
    pgn = open("./data/auerswald.pgn")

    print_init_position()

    count = 1
    while 1:
        game = chess.pgn.read_game(pgn)

        if game is None:
            break

        board = game.board()
        print("value:", round(get_value(board), 4))
        print(board)
        print("s: start, n: next game, q: quit => ", end = "")

        i = input()
        if i == "s":
            pass
        elif i == "n":
            continue
        elif i == "q":
            break

        for move in game.mainline_moves():
            print("move => ", end = "")
            move_player = input()


            val = get_value(board)

            if move.uci() == move_player:
                print("correct!", move, "\nvalue:", round(val, 4))
            else:
                print("false", move, "\nvalue:", round(val, 4))

            board.push(move)
            print(count)
            print(board)
            count += 1

        print("end\n")
        i = input()
        if i == "s":
            pass
        elif i == "n":
            continue
        elif i == "q":
            break
        count = 1

if __name__ == "__main__":
    main()
