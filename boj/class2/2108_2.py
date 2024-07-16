# 통계학
from collections import Counter

n = int(input())
ls = [int(input()) for _ in range(n)]
ls.sort()

# 산술평균
print(round(sum(ls) / n))
# 중앙값
print(ls[n//2])
# 최빈값
top_num = Counter(ls).most_common()
if len(ls) > 1:
    if top_num[0][1] == top_num[1][1]:
        print(top_num[1][0])
    else:
        print(top_num[0][0])
else:
    print(ls[0])
# 범위
print(ls[-1] - ls[0])
