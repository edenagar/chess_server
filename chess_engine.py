import chess


def evaluation(board):
    i = 0
    evaluation = 0

    x = [a for a in str(board).split("\n") if a]
    for i in range(len(x)):
        for j in range(len(x[i])):
            try:
                if x[i][j] == "p":
                    evaluation = evaluation - 10
                if x[i][j] == "P":
                    evaluation = evaluation + 10
                if x[i][j] == "r":
                    evaluation = evaluation - 50
                if x[i][j] == "R":
                    evaluation = evaluation + 50
                if x[i][j] == "n":
                    evaluation = evaluation - 30
                if x[i][j] == "N":
                    evaluation = evaluation + 30
                if x[i][j] == "b":
                    evaluation = evaluation - 30
                if x[i][j] == "B":
                    evaluation = evaluation + 30
                if x[i][j] == "q":
                    evaluation = evaluation - 90
                if x[i][j] == "Q":
                    evaluation = evaluation + 90
                if x[i][j] == "k":
                    evaluation = evaluation - 900
                if x[i][j] == "K":
                    evaluation = evaluation + 900
            except IndexError:
                pass
    return evaluation


def calculate_next_move(board_state):
    board = chess.Board(board_state)
    possible_moves = board.legal_moves
    bestMove = None
    bestValue = -9999
    for x in possible_moves:
        move = chess.Move.from_uci(str(x))
        board.push(move)
        boardValue = -evaluation(board)
        board.pop()
        if boardValue > bestValue:
            bestValue = boardValue
            bestMove = move
    return bestMove.uci()
