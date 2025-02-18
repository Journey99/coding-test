# 블랙잭

n, m = map(int, input().split())
card_nums = list(map(int, input().split()))

max_value = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            total = card_nums[i] + card_nums[j] + card_nums[k]
            if m >= total:
                max_value = max(max_value, total)

print(max_value)
