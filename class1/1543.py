n = int(input())
score = list(map(int, input().split()))
high_score = max(score)
sum = 0

for scr in score:
    sum += scr / high_score * 100

print(sum/n)
