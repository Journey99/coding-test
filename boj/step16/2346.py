from collections import deque

n = int(input())
nums = list(map(int, input().split()))
deq = deque((i+1, num) for i, num in enumerate(nums))  # (풍선 번호, 안 숫자)

result = []

num, move = deq.popleft()
result.append(num)

while deq:
    if move > 0:
        for _ in range(move - 1):
            deq.append(deq.popleft())
        num, move = deq.popleft()
        result.append(num)
    else:
        for _ in range(-move - 1):
            deq.appendleft(deq.pop())
        num, move = deq.pop()
        result.append(num)

print(' '.join(map(str, result)))