# 최종 순위
import sys
from collections import deque
input = sys.stdin.readline

def topology_sort(n):
    queue = deque([i for i in range(1, n+1) if indegree[i] == 0])
    result = []
    certain = True  # 순위를 확정할 수 있는지 여부

    for _ in range(n):
        if not queue:  # 큐가 비었는데 아직 결과가 안 채워짐 → 사이클
            return "IMPOSSIBLE"
        if len(queue) > 1:  # 큐에 여러 개 있으면 확정 불가
            certain = False

        now = queue.popleft()
        result.append(now)

        for nxt in graph[now]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)

    if not certain:
        return "?"
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    lastyear = list(map(int, input().split()))
    m = int(input())

    graph = [[False]*(n+1) for _ in range(n+1)]
    indegree = [0]*(n+1)

    # 작년 순위 기반 그래프 만들기
    for i in range(n):
        for j in range(i+1, n):
            higher, lower = lastyear[i], lastyear[j]
            graph[higher][lower] = True
            indegree[lower] += 1

    # 변경된 순위 반영
    for _ in range(m):
        a, b = map(int, input().split())
        if graph[a][b]:  # a→b 였으면 반대로
            graph[a][b] = False
            graph[b][a] = True
            indegree[b] -= 1
            indegree[a] += 1
        else:  # b→a 였으면 반대로
            graph[b][a] = False
            graph[a][b] = True
            indegree[a] -= 1
            indegree[b] += 1

    # 인접 리스트 변환
    new_graph = [[] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j]:
                new_graph[i].append(j)

    graph = new_graph
    answer = topology_sort(n)

    if isinstance(answer, str):
        print(answer)
    else:
        print(*answer)

    
      
    