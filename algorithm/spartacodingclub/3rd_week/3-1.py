# 미로 탈출 경로 찾기
from collections import deque

maze = input()
maze_graph = [list(map(int, line)) for line in maze.split()]
n, m = len(maze_graph), len(maze_graph[0])

queue = deque([(0,0)])
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        next_x, next_y = x+dx[i], y+dy[i]
        if 0<= next_x < n and 0 <= next_y < m:
            if maze_graph[next_x][next_y] == 1:
                queue.append((next_x, next_y))
                maze_graph[next_x][next_y] = maze_graph[x][y] + 1

print(maze_graph[n-1][m-1])
