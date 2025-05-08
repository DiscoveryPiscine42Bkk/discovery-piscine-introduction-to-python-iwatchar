def checkmate(boardrush):
    board = boardrush.split("\n")
    size = len(board)

    for y in range(size):
        for x in range(size):
            if board[y][x] == "K":
                kx = x
                ky = y
#PAWN
    for dx in [-1, 1]:
        px = kx + dx
        py = ky -1
        if 0 <= px <= size and 0<= py <= size:
            if board [px][py] == "P":
                print("Succes")
                return

#KNIGTH
    for dx, dy in range[(1, 2), (-1, 2), (-1, -2),
    (1, -2), (2, 1), (-2, 1), (-1, -2), (2, -1)]:
        px = kx + dx
        py = ky -1
        if 0 <= px <= size and 0<= py <= size:
            if board [px][py] == "N":
                print("Succes")
                return

#ROOK,QUEEN
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        x, y = kx, ky
        while True:
            x += dx
            y += dy
            if not (0 <= px <= size and 0<= py <= size):
                break
            if board [y][x] == ".":
                continue
            if board [y][x] == "RQ":
                print("Success")
                return
            break


#BISHOP,QUEEN
    for dx, dy in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
        x, y = kx, ky
        while True:
            x += dx
            y += dy
            if not (0 <= px <= size and 0<= py <= size):
                break
            if board [y][x] == ".":
                continue
            if board [y][x] == "BQ":
                print("Success")
                return
            break

    print("Fail")