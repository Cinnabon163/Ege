import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_matrix(mat, name):
    print(f"{name}:")
    for row in mat:
        print(' '.join(map(str, row)))
    print()

def horse_with_display(N, M):
    board = [[0]*M for _ in range(N)]
    board[0][0] = 1
    result = 0
    while True:
        new_board = [[0]*M for _ in range(N)]

        if board == new_board:
            break

        clear_screen()    
        print_matrix(board, "Board")
        
        for i in range(N):
            for j in range(M):
                if board[i][j] != 0:
                    if i+2 < N and 0 <= j-1 < M:
                        new_board[i+2][j-1] += board[i][j]
                    if i+2 < N and j+1 < M:
                        new_board[i+2][j+1] += board[i][j]
                    if i+1 < N and j+2 < M:
                        new_board[i+1][j+2] += board[i][j]
                    if 0 <= i-1 < N and j+2 < M:
                        new_board[i-1][j+2] += board[i][j]
        print_matrix(new_board, "New board")
        board = new_board
        result += new_board[-1][-1]
        time.sleep(3)  
    
    return result

print(horse_with_display(6, 6))

