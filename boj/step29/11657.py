# 타임머신
import heapq, sys
input = sys.stdin.readline

INF = int(1e9)

def bellman_ford(n, edges, start):
    distance = [INF] * (n+1)
    distance[start] = 0

    for _ in range(n-1):
        for u, v, w in edges: # u -> v 가중치 w
            if distance[u] != INF and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
    
    # 음수 사이클 검사
    for u, v, w in edges:
        if distance[u] != INF and distance[u] + w < distance[v]:
            return None
    
    return distance


n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

result = bellman_ford(n, edges, 1)

if result is None:
    print(-1)
else:
    for i in range(2, n+1):
        if result[i] != INF:
            print(result[i])
        else:
            print(-1)
