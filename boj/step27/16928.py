# 뱀과 사다리 게임
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lader, snake = {}, {}

for _ in range(n):
    x, y = map(int, input().split())
    lader[x] = y

for _ in range(m):
    x, y = map(int, input().split())
    snake[x] = y

visitied = [False] * 101
dice = [1, 2, 3, 4, 5, 6]

queue = deque()
queue.append((1, 0)) # 첫번째 칸, 횟수
visitied[1] = True

while queue:
    x, cnt = queue.popleft()

    if x == 100:
        print(cnt)
        exit(0)

    for d in dice:
        nx = x + d
        if 0 < nx <= 100 and not visitied[nx]:
            if nx in lader:
                nx = lader[nx]
            elif nx in snake:
                nx = snake[nx]
            
            if not visitied[nx]:
                queue.append((nx, cnt+1))
                visitied[nx] = True
