import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    visited[x][y] = True

    dx = [-1, 1, 0, 0]  # 행 이동
    dy = [0, 0, -1, 1]  # 열 이동

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1  # 행=y, 열=x

    result = 0
    for i in range(n):  # 행
        for j in range(m):  # 열
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                result += 1

    print(result)
