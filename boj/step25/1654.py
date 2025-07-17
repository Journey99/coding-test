# 랜선 자르기
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lengths = [int(input()) for _ in range(k)]
start = 1
end = max(lengths)
answer = 0

while start <= end:
    mid = (start + end) // 2
    cnt = sum(l // mid for l in lengths)

    if cnt >= n:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)


