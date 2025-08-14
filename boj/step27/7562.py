# 나이트의 이동
from collections import deque
import sys
input = sys.stdin.readline

def bfs(startx, starty):
    queue = deque()
    queue.append((startx, starty, 0))
    visited[startx][starty] = True

    while queue:
        x, y, cnt = queue.popleft()

        if x == endx and y == endy:
            return cnt

        moves = [
            (-2, -1), (-2, 1),
            (-1, -2), (-1, 2),
            (1, -2),  (1, 2),
            (2, -1),  (2, 1)
        ]
        
        for dx, dy in moves:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, cnt+1))
        


t = int(input())
for _ in range(t):
    l = int(input())
    visited = [[False] * l for _ in range(l)]

    startx, starty = map(int, input().split())
    endx, endy = map(int, input().split())

    print(bfs(startx, starty))