# 연산자 끼워넣기
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

max_result = -float('inf')
min_result = float('inf')

def calc(a, b, op):
    if op == 0:
        return a + b
    elif op == 1:
        return a - b
    elif op == 2:
        return a * b
    elif op == 3:
        if a < 0:
            return -(-a//b)
        return a // b

def dfs(idx, current_result):
    global max_result, min_result

    if idx == n:
        max_result = max(max_result, current_result)
        min_result = min(min_result, current_result)
        return
    
    for i in range(4):
        if ops[i] > 0:
            ops[i] -= 1
            next_result = calc(current_result, nums[idx], i)
            dfs(idx+1, next_result)
            ops[i] += 1


dfs(1, nums[0])  # 시작은 nums[0], 다음은 nums[1]부터
print(max_result)
print(min_result)