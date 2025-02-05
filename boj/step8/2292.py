# 벌집
n = int(input())
cnt = 1
box_maxnum = 1

while n > box_maxnum:
    box_maxnum += 6 * cnt
    cnt += 1
print(cnt)

## 위의 코드 반대로
while n > 1:
    n -= (6*cnt)
    cnt += 1