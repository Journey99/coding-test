# DFS와 BFS

from collections import deque

N, M, V = list(map(int, input().split()))
matrix = [[0 for i in range(N+1)] for i in range(N+1)]
dfs_answer = []
bfs_answer = []
visited = [False for i in range(N + 1)]
visit = [False for i in range(N + 1)]

## 인접 행렬 방식으로 입력받기.
for i in range(M):
	x, y = map(int, input().split())
	matrix[x][y] = matrix[y][x] = 1

def dfs(V) :
	dfs_answer.append(str(V))
	visited[V] = True
	for i in range(1, N + 1) :
		if visited[i] == False and matrix[V][i] == 1 :
			dfs(i)

queue = deque()

def bfs(V):
	visit[V] = True
	queue.append(V)

	while (queue) :
		V = queue.popleft()
		bfs_answer.append(str(V))

		for i in range(1, N+1):
			if visit[i] == False and matrix[V][i] == 1 :
				queue.append(i)
				visit[i] = True

dfs(V)
bfs(V)
print(" ".join(dfs_answer))
print(" ".join(bfs_answer))