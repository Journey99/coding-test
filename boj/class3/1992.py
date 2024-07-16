# 쿼드트리

import sys

input = sys.stdin.readline
n = int(input())
graph = [list(map(str, input().rstrip())) for _ in range(n)]
# 시작점의 좌표와 조사할 크기를 매개변수로
def dfs(x, y, size):
    if size == 1:
        return graph[x][y]
    # 전부 0 혹은 1인지 검사
    count = 0
    for i in range(x, x + size):
        for j in range(y, y + size):
            count += int(graph[i][j])
    if count == 0 or count == size ** 2:
        return "0" if count == 0 else "1"
    halfsize = size // 2
    return (
        "("
        + dfs(x, y, halfsize)
        + dfs(x, y + halfsize, halfsize)
        + dfs(x + halfsize, y, halfsize)
        + dfs(x + halfsize, y + halfsize, halfsize)
        + ")"
    )


print(dfs(0, 0, n))