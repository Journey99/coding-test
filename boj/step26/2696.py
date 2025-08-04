# 중앙값 구하기
'''
중앙값을 기준으로 왼쪽에는 max_heap , 오른쪽에는 min_heap 을 만든다
중앙값은 항상 max_heap 의 루트에!

ex) 1 5 2 10 7 일 때
1. max_heap : [1] / min_heap : [] / 중앙값 : 1
2. max_heap : [1] / min_heap : [5] / 중앙값 : 1 (짝수번째니까 중앙값 안구함/안바뀜)
3. max_heap : [2, 1] / min_heap : [5] / 중앙값 : 2 
-> 새 숫자 2는 중앙값 1보다 크니까 min_heap에 넣어야 하는데 min_heap의 크기가 max_heap의 크기보다 크기 때문에 하나 빼서 옮긴다

'''
import sys
import heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m = int(input())    
    nums = []

    while len(nums) < m:
        nums.extend(map(int, input().split()))

    max_heap = []
    min_heap = []
    result = []

    for i, n in enumerate(nums):
        # 처음 넣을 때 또는 중앙값 이하일 때
        if not max_heap or n <= -max_heap[0]:
            heapq.heappush(max_heap, -n)
        else:
            heapq.heappush(min_heap, n)

        # 균형 맞추기
        if len(max_heap) > len(min_heap) + 1:
             heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        # 홀수 번째일 때 중앙값 저장
        if i % 2 == 0:
            result.append(-max_heap[0])

    print(len(result))
    for i in range(0, len(result), 10):
        print(*result[i:i+10])           
