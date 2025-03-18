# 문자열 집합
import sys

n, m = map(int, input().split())
answer = set()
cnt = 0

for _ in range(n):
    answer.add(sys.stdin.readline())

for _ in range(m):
    check_str = sys.stdin.readline()
    if check_str in answer:
        cnt += 1

print(cnt)