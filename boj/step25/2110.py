# 공유기 설치
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
cords = sorted([int(input()) for _ in range(n)])

def can_install(distance):
    cnt = 1
    location = cords[0] # 공유기 처음 놓는 위치

    for i in range(1, n):
        if cords[i] - location >= distance:
            cnt += 1
            location = cords[i] # 놓는 위치 갱신
    
    return cnt >= c

# 이분 탐색 범위
start = 1
end = cords[-1] - cords[0]
result = 0

while start <= end:
    mid = (start + end) // 2

    if can_install(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)