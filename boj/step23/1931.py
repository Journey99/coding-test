# 회의실 배정

import sys
input = sys.stdin.readline

n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]

# 끝나는 시간 기준 정렬 (같으면 시작 시간 기준)
times.sort(key=lambda x: (x[1], x[0]))

cnt = 1
last_end = times[0][1]

for start, end in times[1:]:
    if start >= last_end:
        cnt += 1
        last_end = end

print(cnt)
