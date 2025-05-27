# N-Queen

def Check(depth):
    for i in range(depth):
        # 세로선상과 대각선상에 다른 퀸이 존재할 경우
        if board[depth] == board[i] or abs(board[depth] - board[i]) == depth - i:
            return False
    return True

# N개의 퀸을 서로 공격하지 않게 놓기 위한 DFS 탐색
def DFS(depth):
    global result
    
    # N개의 퀸을 서로 공격하지 않게 놓은 경우
    if depth == N:
        result += 1
        return

    else:
        for i in range(N):
            board[depth] = i
            if Check(depth):
                DFS(depth + 1)


N = int(input())
board = [0 for i in range(N)]
result = 0

DFS(0)
print(result)
