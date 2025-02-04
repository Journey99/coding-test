# 최댓값

## 2차원 배열 사용안하고 했을 경우
max_num = 0
r, c = 0, 0
for i in range(9):
    m = list(map(int, input().split()))
    if max(m) >= max_num:
        max_num = max(m)
        r = i+1
        c = m.index(max_num) + 1

print(max_num)
print(r, c)


## 2차원 배열 사용했을 경우
table = [list(map(int, input().split())) for _ in range(9)]

max_num = 0
max_row, max_col = 0, 0
for row in range(9):
    for col in range(9):
        if max_num <= table[row][col]:
            max_row = row + 1
            max_col = col + 1
            max_num = table[row][col]

print(max_num)
print(max_row, max_col)