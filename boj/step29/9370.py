# 미확인 도착지
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, n, graph):
    dist = [INF] * (n+1)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        cost, now = heapq.heappop(heap)
        if dist[now] < cost:
            continue
        for nxt, w in graph[now]:
            new_cost = cost + w
            if new_cost < dist[nxt]:
                dist[nxt] = new_cost
                heapq.heappush(heap, (new_cost, nxt))
    return dist

T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))

    candidates = [int(input()) for _ in range(t)]

    dist_s = dijkstra(s, n, graph)
    dist_g = dijkstra(g, n, graph)
    dist_h = dijkstra(h, n, graph)

    ans = []
    for x in candidates:
        path1 = dist_s[g] + dist_g[h] + dist_h[x]
        path2 = dist_s[h] + dist_h[g] + dist_g[x]
        shortest = dist_s[x]

        if shortest == min(path1, path2):
            ans.append(x)

    ans.sort()
    print(*ans)
