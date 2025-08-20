# 특정한 최단 경로
'''
방향성이 없는 그래프
임의의 주어진 두 정점은 반드시 통과해야 함
한번 이동했던 정점, 간선 다시 이동할 수 있음
반드시 최단 경로로 이동해야함
'''
import sys
import heapq
input = sys.stdin.readline

def dijkstra(start, n, graph):
    distance = [float("inf")] * (n+1)
    distance[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))

    cnt = {v1:0, v2:0} # 반드시 지나야 하는 점

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for nxt, w in graph[now]:
            cost = dist + w
            if cost < distance[nxt]:
                if nxt == v1 or nxt == v2:
                    cnt[nxt] += 1
                distance[nxt] = cost
                heapq.heappush(heap, (cost, nxt))

    return distance

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1, v2 = map(int, input().split())

# 각 구간 최단 거리 계산
dist_from_1 = dijkstra(1, n, graph)
dist_from_v1 = dijkstra(v1, n , graph)
dist_from_v2 = dijkstra(v2, n, graph)

# 1 → v1 → v2 → n
path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[n]
# 1 → v2 → v1 → n
path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[n]

answer = min(path1, path2)

if answer >= float("inf"):
    print(-1)
else:
    print(answer)