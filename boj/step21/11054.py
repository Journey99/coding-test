# 가장 긴 바이토닉 부분 수열
'''
바이토닉 수열 : 오름차순 -> 내림차순
각 위치를 기준으로 왼쪽은 증가, 오른쪽은 감소
두번의 dp 필요
left[i] ; i를 끝으로 하는 lis길이
right[i] ; i를 시작으로 하는 lds 길이

1. 각 인덱스를 기준으로 왼쪽은 LIS, 오른쪽은 LDS를 구함
2. 각 인덱스 i에서: LIS[i] + LDS[i] - 1 → 바이토닉 수열의 최대 길이
3. 전체에서 가장 긴 바이토닉 수열을 출력
'''

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

up = [1] * n
down = [1] * n

# 증가하는 부분 수열
for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            up[i] = max(up[i], up[j] + 1)

# 감소하는 부분 수열
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if a[i] > a[j]:
            down[i] = max(down[i], down[j] + 1)

# 바이토닉 수열 길이 계산
max_len = 0
for i in range(n):
    max_len = max(max_len, up[i] + down[i] - 1)

print(max_len) 



