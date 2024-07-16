# 좌표 증가순으로 정렬

n = int(input())
array = []

for i in range(n):
    x, y = map(int, input().split())
    array.append((x, y))

array.sort(key = lambda x : (x[0], x[1]))

for e in array:
    print(e[0], e[1])
