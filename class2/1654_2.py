# 랜선 자르기

# 입력 시간을 줄이기 위해 sys.stdin.readline() 사용
import sys

x, n = sys.stdin.readline().split()
x, n = int(x), int(n)

# 랜선의 길이가 들어갈 list : l, 정답이 들어갈 변수 m
l = [];
m = 0

# x의 크기만큼 랜선의 길이 입력받아 list에 append
for _ in range(x):
    l.append(int(sys.stdin.readline()))

# 이분탐색을 위해 high = 리스트 l에서 제일 큰 값
low = 0;
high = max(l)

# 이분탐색
while low <= high:
    mid = (high + low + 1) // 2
    ans = 0

    # ans = 랜선이 잘라지고 남은 개수들의 합
    for j in l: ans += (j // mid)

    # 조건에 따라 탐색 범위를 좁혀감
    if ans >= n:
        low = mid + 1
        if mid > m: m = mid
    else:
        high = mid - 1
print(m)