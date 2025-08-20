# 문제집
'''
- n개의 문제는 모두 풀어야 한다
- 먼저 푸는 것이 좋은 문제가 있는 문제는, 먼저 푸는 것이 좋은 문제를 반드시 먼저 푼다
- 가능하면 쉬운 문제부터 풀어야 한다
우선 순위 : 쉬운 문제 > 먼저푸는거
'''

import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

heap = []
for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

result = []

while heap:
    x = heapq.heappop(heap)
    result.append(x)

    for nxt in graph[x]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heapq.heappush(heap, nxt)
    
print(*result)
