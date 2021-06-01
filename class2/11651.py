# 좌표 정렬하기 - y가 증가하는 순으로 , 그다음 x가 증가하는 순

n = int(input())
axis = []
for i in range(n):
    x, y = map(int, input().split())
    axis.append((x, y))

axis.sort(key = lambda y: (y[1], y[0]))

for e in axis:
    print(e[0], e[1])



