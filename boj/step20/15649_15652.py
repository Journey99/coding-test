# 15649 ; n과 m (1)
# 15650 ; n과 m (2)
# 15651 ; n과 m (3)
# 15652 ; n과 m (4)


# 순열
def backtrack_15649(depth):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            backtrack_15649(depth + 1)
            result.pop()
            visited[i] = False

# 조합
def backtrack_15650(start, depth):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(start, N + 1):
        result.append(i)
        backtrack_15650(i+1, depth+1)
        result.pop()

# 중복순열
def backtrack_15651(depth):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(1, N + 1):
        result.append(i)
        backtrack_15651(depth+1)
        result.pop()

# 중복조합
def backtrack_15652(start, depth):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(start, N + 1):
        result.append(i)
        backtrack_15650(i, depth+1)
        result.pop()

N, M = map(int, input().split())

visited = [False] * (N + 1)
result = []

backtrack_15649(0)
backtrack_15650(1, 0)
backtrack_15651(0)
backtrack_15652(1, 0)





############################################################################################################

from itertools import permutations, combinations, product, combinations_with_replacement

arr = [1, 2, 3]
r = 2

print("순열:", list(permutations(arr, r)))
print("조합:", list(combinations(arr, r)))
print("중복 순열:", list(product(arr, repeat=r)))
print("중복 조합:", list(combinations_with_replacement(arr, r)))
