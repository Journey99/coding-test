# 숫자카드2
import sys
from collections import Counter

n = int(input())
get_cards = list(map(int, sys.stdin.readline().split()))
get_cards_dic = dict(Counter(get_cards))

m = int(input())
cards = list(map(int, sys.stdin.readline().split()))

for c in cards:
    print(get_cards_dic.get(c, 0), end=" ")


# get_cards_dic = {}
# for card in get_cards:
#     get_cards[card] += 1