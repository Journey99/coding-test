# 좌표 정렬하기 2

n = int(input())
cords = []
for _ in range(n):
    x, y = map(int, input().split())
    cords.append((x,y))

cords.sort(key= lambda x : (x[1], x[0]))

for cord in cords:
    print(*cord)