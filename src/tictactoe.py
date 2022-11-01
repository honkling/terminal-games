from msilib.schema import Error


board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

def display():
    print("\n" * 150)
    print("-------")

    for row in board:
        display = []

        for col in range(0, 3):
            display.append([" ", "x", "o"][row[col]])

        print("|%s|%s|%s|" % (display[0], display[1], display[2]))

    print("-------")

def check():
    for player in range(1, 3):
        for i in range(0, 3):
            if board[i] == [player] * 3:
                return player

            verticalWin = player
            for o in range(0, 3):
                if board[o][i] != player:
                    verticalWin = False

            if verticalWin != False:
                return player

            if [
                board[0][0],
                board[1][1],
                board[2][2],
            ] == [player] * 3:
                return player

            if [
                board[0][2],
                board[1][1],
                board[2][0],
            ] == [player] * 3:
                return player

    return False

turn = 1
winner = None

while not (winner := check()):
    display()
    try:
        inp = input().split(", ")
        x = int(inp[0]) - 1
        y = int(inp[1]) - 1
    except IndexError:
        continue
    except ValueError:
        continue
    except KeyboardInterrupt:
        exit()

    if x < 0 or x > 2 or not 0 in board[x]:
        continue

    board[y][x] = turn
    turn = 2 if turn == 1 else 1

display()
print("%s wins!" % ("Player 1" if winner == 1 else "Player 2"))
