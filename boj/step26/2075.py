# n번째 큰 수
'''
python의 heapq : heqp[0]은 항상 가장 작은값. 그 외의 순서는 정렬된 것처럼 보이지 않음
'''
import heapq
import sys
input = sys.stdin.readline

n = int(input())
pq = []

for _ in range(n):
    nums = list(map(int, input().split()))
    for num in nums:
        if len(pq) < n:
            heapq.heappush(pq, num)
        else:
            if num > pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, num)

print(pq[0])

