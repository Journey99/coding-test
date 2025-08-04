# 보석 도둑
'''
보석이 총 n개
각 보석은 무게 M, 가격 V 를 가지고 있음
가방 k개를 가지고 있고 각 가방에 담을 수 있는 최대 무게는 Ci (가방에는 한개의 보석만)
훔칠 수 있는 보석의 최대 가격은?
'''

import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
jewelry = []
bags = []

for _ in range(n):
    m, v = map(int, input().split())
    jewelry.append((m, v))

bags = [int(input()) for _ in range(k)]

jewelry.sort() # 무게 기준 오름차순
bags.sort() # 가방 무게 오름차순

result = 0
idx = 0
tmp = [] # 후보 보석

for bag in bags:
    # 가방에 넣을 수 있는 모든 보석 후보를 힙에 넣음
    while idx < n and jewelry[idx][0] <= bag:
        heapq.heappush(tmp, -jewelry[idx][1]) # 가격 최대 힙
        idx += 1

    # 가장 비싼 보석을 꺼내서 결과에 더함
    if tmp:
        result += -heapq.heappop(tmp)

print(result) 
