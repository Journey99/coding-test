# 커트라인

n, k = map(int, input().split())
scores = sorted(map(int, input().split()))[::-1]
print(scores[k-1])
