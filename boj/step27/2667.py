# 단지번호붙이기
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    global count

    visited[x][y] = True
    count += 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)


n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
result = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            count = 0
            dfs(i, j)
            result.append(count)

result.sort()
print(len(result))
for r in result:
    print(r)