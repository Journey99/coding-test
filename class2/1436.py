import sys

n = int(input())

name = 666
cnt = 0
while True:
    if '666' in str(name):
        cnt += 1
        if cnt == n:
            print(name)
            break

    name += 1

# 알고리즘 중 브루트 포스를 이용한 문제
# 666부터 시작해서 하나씩 증가하면서 일치하는지 확인