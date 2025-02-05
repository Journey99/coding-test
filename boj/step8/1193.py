# 분수찾기
n = int(input())

row = 1
result = ''

while n > row:
    n -= row
    row += 1 # 줄 추가

if row % 2 == 1:
    number = row - n + 1
    denom = n
else:
    number = n
    denom = row - n + 1

result = f"{number}/{denom}"
print(result)