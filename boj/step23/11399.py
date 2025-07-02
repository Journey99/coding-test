# ATM
import sys
input = sys.stdin.readline

n = int(input())
times = list(map(int, input().split()))
times.sort()
total_time = 0

for i in range(n):
    total_time += times[i] * (n-i)

print(total_time)