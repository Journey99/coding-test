# 파도반 수열
import sys
input = sys.stdin.readline
results = [0, 1, 1, 1] + [0 for _ in range(97)]

def padovan(n):
    if results[n]:
        return results[n]

    results[n] = padovan(n-3) + padovan(n-2)
    return results[n]

t = int(input())
for _ in range(t):
    n = int(input())
    print(padovan(n))



'''
1 1 1 2 2 3 4 5 7 9


'''