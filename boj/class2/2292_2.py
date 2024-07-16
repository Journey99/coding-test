# 벌집

n = int(input())
cnt = 1
num = 1

while True:
    if num >= n:
        break
    num += 6*cnt
    cnt += 1

print(cnt)