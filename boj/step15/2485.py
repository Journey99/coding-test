# 가로수
import sys

def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n%m)

n = int(input())
trees = []
between_trees = []

for i in range(n):
    trees.append(int(int(sys.stdin.readline().strip())))
    if i > 0:
        between_trees.append(trees[i] - trees[i-1])

for i in range(len(between_trees)):
    if i == 0:
        gcd_value = between_trees[i]
    else:
        gcd_value = gcd(gcd_value, between_trees[i])


new_trees = (trees[-1] - trees[0]) // gcd_value + 1 - len(trees)
print(new_trees)