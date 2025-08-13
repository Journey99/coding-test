# 바이러스
import sys
input= sys.stdin.readline

def dfs(v):
    visited[v] = True

    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor)

num = int(input())
pair = int(input())
graph = [[] for _ in range(num+1)]

for _ in range(pair):
    c1, c2 = map(int, input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)


visited = [False] * (num+1)
dfs(1)

print(sum(visited)-1)
