# 주유소
import sys
input = sys.stdin.readline

n = int(input()) # 도시의 개수
distance = list(map(int, input().split())) # 도로의 길이
price = list(map(int, input().split())) # 주유 가격

total_cost = 0
min_price = price[0]

for i in range(n-1):
    if min_price > price[i]:
        min_price = price[i]
    total_cost += min_price * distance[i]

print(total_cost)

