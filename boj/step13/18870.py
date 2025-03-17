# 좌표 압축
import sys

n = int(input())
x_cord = list(map(int, sys.stdin.readline().split()))
sorted_x_cord = sorted(x_cord)

for x in x_cord:
    print(sorted_x_cord.index(x), end=' ')

## 위의 코드는 시간초과 발생
## index(x)는 O(N)의 시간복잡도를 가지는데 for문을 돌면 O(N^2)의 시간복잡도를 가지게 됨

import sys

n = int(input())
x_cord = list(map(int, sys.stdin.readline().split()))

sorted_x_cord = sorted(set(x_cord))
index_map = {value: idx for idx, value in enumerate(sorted_x_cord)}

for x in x_cord:
    print(index_map[x], end=' ')