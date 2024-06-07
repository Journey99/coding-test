# 10807
n = int(input())
ls = list(map(int, input().split()))
v = int(input())
cnt = 0
for i in ls:
    if i == v:
        cnt += 1

print(cnt)

"""
# 내장함수 사용
print(ls.count(v))
"""


# 10871
n, x = map(int, input().split())
a = list(map(int, input().split()))
for i in a:
    if i < x:
        print(i)


# 10818
n = int(input())
ls = list(map(int, input().split()))
print(f'{min(ls)} {max(ls)}')


2562
max_value = 0
key = 0
for i in range(9):
    x = int(input())
    if x > max_value:
        max_value = x
        key = i+1
print(max_value)
print(key)

"""
# list 사용
num_list = []
for i in range(9) :
    num_list.append(int(input()))  	
print(max(num_list))					
print(num_list.index(max(num_list))+1)
"""


# 10810
n, m = map(int, input().split())
basket = [0 for i in range (n)]

for _ in range(m):
    i, j, k = map(int, input().split())
    for idx in range(i-1, j):
        basket[idx] = k

print(*basket)
