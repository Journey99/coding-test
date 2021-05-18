import sys
from collections import Counter

n = int(sys.stdin.readline())
number = []

for _ in range(n):
    number.append(int(sys.stdin.readline()))


def mean(num):
    return round(sum(num) / len(num))

def median(num):
    num.sort()
    mid = num[len(num) // 2]

    return mid

def mode(num):
    mode_dict = Counter(num)
    modes = mode_dict.most_common()

    if len(num) > 1:
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else:
            mod = modes[0][0]
    else:
        mod = modes[0][0]

    return mod

def scope(num):
    return max(num) - min(num)

print(mean(number))
print(median(number))
print(mode(number))
print(scope(number))
