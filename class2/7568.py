# 덩치 순서 나타내기

n = int(input())
ls = []

for i in range(n):
    ls.append(input().split())

seq = []

for i in range(len(ls)):
    cnt = 1
    for j in range(len(ls)):
        if ls[i][0] < ls[j][0] and ls[i][1] < ls[j][1]:
            cnt += 1

    seq.append(cnt)

for i in seq:
    print(i, end=" ")
