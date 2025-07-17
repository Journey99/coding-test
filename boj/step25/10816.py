# 숫자 카드 2
from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
counter = dict(Counter(nums))

m = int(input())
targets = list(map(int, input().split()))

for t in targets:
    try:
        print(counter[t], end=' ')
    except:
        print(0, end=' ')

# 메모리 : 131484 / 시간 : 900 ms
#################################################
# 메모리 : 130040 / 시간 : 740 ms

n = int(input())
get_cards = list(map(int, sys.stdin.readline().split()))
get_cards_dic = dict(Counter(get_cards))

m = int(input())
cards = list(map(int, sys.stdin.readline().split()))

for c in cards:
    print(get_cards_dic.get(c, 0), end=" ")