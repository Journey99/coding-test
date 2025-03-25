# 듣보잡
import sys

n, m = map(int, input().split())
nothear_ls = set()
notlook_ls = []

for _ in range(n):
    nothear_ls.add(sys.stdin.readline().strip())

for _ in range(m):
    notlook_ls.append(sys.stdin.readline().strip())

cnt = 0
result = []
for notlook in notlook_ls:
    if notlook in nothear_ls:
        cnt += 1
        result.append(notlook)

result.sort()
print(cnt)
for r in result:
    print(r)


## 집합 이용
import sys

n, m = map(int, input().split())

hear = [sys.stdin.readline().rstrip() for i in range(n)]
see = [sys.stdin.readline().rstrip() for i in range(m)]

hear_see = list(set(hear) & set(see))
hear_see.sort()

print(len(hear_see))
for i in hear_see:
    print(i)