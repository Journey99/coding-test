# 이중 우선순위 큐

import heapq
from collections import defaultdict
from sys import stdin

input = stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    min_arr = []
    max_arr = []
    dic = defaultdict(int)
    cnt = 0
    for i in range(N):
        cmd, num = input().rstrip().split()
        if cmd == "I":
            cnt += 1
            dic[int(num)] += 1
            heapq.heappush(min_arr, int(num))
            heapq.heappush(max_arr, -int(num))
        else:
            if num == "1":
                while max_arr:
                    key = -heapq.heappop(max_arr)
                    if dic.get(key):
                        dic[key] -= 1
                        break
            else:
                while min_arr:
                    key = heapq.heappop(min_arr)
                    if dic.get(key):
                        dic[key] -= 1
                        break

    ans = [key for key, value in dic.items() if value > 0]
    if ans:
        ans.sort()
        print(ans[-1], ans[0])
    else:
        print("EMPTY")

