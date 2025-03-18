# 숫자 카드
import sys

n = int(input())
get_cards = set(map(int, sys.stdin.readline().split()))

m = int(input())
cards = list(map(int, sys.stdin.readline().split()))

for c in cards:
    print(1 if c in get_cards else 0, end=' ')
