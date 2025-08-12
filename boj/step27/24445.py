# 알고리즘 수업 - 너비 우선 탐색 2

# 알고리즘 수업 - 너비 우선 탐색1
from collections import deque
import sys
input = sys.stdin.readline

def dfs(v):
    global order
    queue = deque([v])
    visited[v] = order

    while queue:
        x = queue.popleft()
        for neighbor in graph[x]:
            if visited[neighbor] == 0:
                order += 1
                visited[neighbor] = order
                queue.append(neighbor)
               

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for g in graph:
    g.sort(reverse=True)

visited = [0] * (n+1)
order = 1

dfs(r)

for i in range(1, n+1):
    print(visited[i])