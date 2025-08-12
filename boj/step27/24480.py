# 알고리즘 수업 - 깊이 우선 탐색 2
import sys
sys.setrecursionlimit(10**6) 
input = sys.stdin.readline

def dfs(v):
    global order

    visited[v] = order

    for neighbor in graph[v]:
        if visited[neighbor] == 0:
            order += 1
            dfs(neighbor)

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

