# 좌표 정렬하기

n = int(input())
cords = [tuple(map(int, input().split())) for _ in range(n)]

cords.sort()

for cord in cords:
    print(*cord)