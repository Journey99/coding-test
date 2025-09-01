# 최단경로
import heapq
import sys
input = sys.stdin.readline

def dijkstra(start, n, graph):
    distance = [float("inf")] * (n+1)
    distance[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for nxt, w in graph[now]:
            cost = dist + w
            if cost < distance[nxt]:
                distance[nxt] = cost
                heapq.heappush(heap, (cost, nxt))
    
    return distance


v, e = map(int, input().split())
k = int(input()) # 시작 정점
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

result = dijkstra(k, v, graph)

for i in range(1, v+1):
    if result[i] == float("inf"):
        print("INF")
    else:
        print(result[i])

