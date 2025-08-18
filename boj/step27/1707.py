# 이분 그래프
from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, color):
    color_ls[x] = color
    for neighbor in graph[x]:
        if color_ls[neighbor] == 0:
            if not dfs(neighbor, -color):
                return False
        elif color_ls[neighbor] == color_ls[x]:
            return False
    
    return True

def bfs(start, graph, color):
    queue = deque([start])
    color[start] = 1  # 시작은 빨강(1)

    while queue:
        node = queue.popleft()
        for nxt in graph[node]:
            if color[nxt] == 0:  # 아직 색칠 안 했으면 반대 색으로
                color[nxt] = -color[node]
                queue.append(nxt)
            elif color[nxt] == color[node]:  # 이미 색칠했는데 같은 색이면 이분 그래프 아님
                return False
    return True

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    color_ls = [0] * (v+1) # 0 : 미방문 , 1/-1 : 색
    is_bipartitie = True

    for i in range(1, v+1):
        if color_ls[i] == 0:
            if not dfs(i, 1):
                is_bipartitie = False
                break
    
    print("YES" if is_bipartitie else "NO")

