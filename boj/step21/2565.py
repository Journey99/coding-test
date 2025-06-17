# 전깃줄
import sys
input = sys.stdin.readline

n = int(input()) # 두 전봇대 사이의 전깃줄의 개수
nums = []
up = [1] * n

for _ in range(n):
    nums.append(tuple(map(int, input().split())))

nums.sort() # a 좌표 정렬
b_list = [b for a, b in nums]

for i in range(n):
    for j in range(i):
        if b_list[i] > b_list[j]:
            up[i] = max(up[i], up[j]+1)

print(n-max(up))

