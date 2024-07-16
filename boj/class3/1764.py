# 듣보잡

from collections import Counter

N, M = map(int, input().split())
No = []
No_SS = []
for i in range(N + M):
    No.append(input())

No_count = Counter(No)
key_list = list(No_count.keys())
value_list = list(No_count.values())
result = 0

for i in range(len(value_list)):
    if value_list[i] == 2:
        No_SS.append(key_list[i])
        result += 1

print(result)
No_SS.sort()
[print(x) for x in No_SS]