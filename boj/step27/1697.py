# 숨바꼭질
'''
이동할 수 있는 경우의 수
x-1 , x+1, 2x

'''

from collections import deque


def bfs(start):
    queue = deque()
    queue.append((start, 0))
    visited[start] = True

    while queue:
        pos, time = queue.popleft()

        if pos == k:
            return time 

        for npos in [pos+1, pos-1, 2*pos]:
            if 0 <= npos <= max_pos and not visited[npos]:
                visited[npos] = True
                queue.append((npos, time+1))


n, k = map(int, input().split())
max_pos = 100000
visited = [False] * (max_pos + 1)

print(bfs(n))
