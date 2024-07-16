# 연결요소의 개수

import sys
input = sys.stdin.readline

n, m = map(int,input().rstrip().rsplit())
graph, visited = {}, [0]*(n+1)
cnt = 0

for _ in range(m):
    u,v = map(int,input().rstrip().rsplit())
    if u not in graph:
        graph[u] = [v]
    else:
        graph[u].append(v)

    if v not in graph:
        graph[v] = [u]
    else:
        graph[v].append(u)

def dfs(u):
    visited[u] = 1
    if u in graph:
        for v in graph[u]:
            if visited[v] == 0:
                dfs(v)

    return 1

for i in range(1,n+1):
    if visited[i] == 0:
        cnt += dfs(i)

print(cnt)