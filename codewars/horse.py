def horse(N:int, M:int):
    board = [[0]*M for _ in range(N)]
    board[0][0] = 1
    # [N-1][M-1]

    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                if i+2 < N and j+1 < M:
                    board[i+2][j+1] += board[i][j]
                if i+1 < N and j+2 < M:
                    board[i+1][j+2] += board[i][j]
    return board, board[N-1][M-1]

h = horse(12, 11)

for l in h[0]:
    print(l)

print(h[1])

