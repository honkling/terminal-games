board = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

def display():
    print("\n" * 150)
    for i in range(0, 4):
        display = []
        for o in range(0, 4):
            display.append([" ", "x", "o"][board[o][i]])
        #print(display)
        print("|%s|%s|%s|%s|" % (display[0], display[1], display[2], display[3]))
    print("---------")

def check():
    for player in range(1, 3):
        for i in range(0, 4):
            if board[i] == [player] * 4:
                return player

            verticalWin = player
            for o in range(0, 4):
                if board[o][i] != player:
                    verticalWin = False

            if verticalWin != False:
                return player

            if [
                board[0][0],
                board[1][1],
                board[2][2],
                board[3][3]
            ] == [player] * 4:
                return player

            if [
                board[0][3],
                board[1][2],
                board[2][1],
                board[3][0]
            ] == [player] * 4:
                return player

    return False

turn = 1
winner = None

while not (winner := check()):
    display()
    try:
        x = int(input()) - 1
    except ValueError:
        continue
    except KeyboardInterrupt:
        exit()

    if x < 0 or x > 3 or not 0 in board[x]:
        continue

    for i in reversed(range(0, 4)):
        if board[x][i] == 0:
            board[x][i] = turn
            turn = 2 if turn == 1 else 1
            break

display()
print("%s wins!" % ("Player 1" if winner == 1 else "Player 2"))
