# 하노이 워프
## 임의의 원판을 워프시킨 후, 남은 원판을 최소 이동 횟수로 옮기는데 필요한 이동 횟수 구하기
cache = [0] * 1001

def hanoi(n):
    if cache[n] != 0:
        return cache[n]
    
    if n == 1:
        return 1
    if n == 0:
        return 0

    cache[n] = 2 * hanoi(n-1) + 1
    return cache[n]


n = int(input())
k = int(input())
answer = hanoi(n) - hanoi(k) + hanoi(k-1)
print(answer)