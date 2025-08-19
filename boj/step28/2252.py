# 줄 세우기
from collections import deque

n, m = map(int, input().split()) # n : 학생 수 / m : 키를 비교한 횟수
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split()) # a 가 b 앞에 서야 함
    graph[a].append(b)
    indegree[b] += 1

queue = deque([i for i in range(1, n+1) if indegree[i] == 0])
result = []

while queue:
    x = queue.popleft()
    result.append(x)

    for nxt in graph[x]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)


print(*result)

