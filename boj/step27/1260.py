# dfs와 bfs
from collections import deque
import sys
input = sys.stdin.readline

def dfs(v):
    visited_dfs[v] = True
    result_dfs.append(v)

    for neighbor in graph[v]:
        if not visited_dfs[neighbor]:
            dfs(neighbor)

def bfs(v):
    queue = deque([v])
    visited_bfs[v] = True

    while queue:
        x = queue.popleft()
        result_bfs.append(x)

        for neighbor in graph[x]:
            if not visited_bfs[neighbor]:
                visited_bfs[neighbor] = True
                queue.append(neighbor)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for g in graph:
    g.sort()

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)
result_dfs = []
result_bfs = []

dfs(v)
print(*result_dfs)
bfs(v)
print(*result_bfs)



