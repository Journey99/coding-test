# 약수 구하기
## n과 k가 주어졌을 때, n의 약수들 중 k번째로 작은 수를 출력

n, k = map(int, input().split())
result = []
for i in range(1, n+1):
    if n % i == 0:
        result.append(i)

if len(result) < k:
    print(0)
else:
    print(result[k-1])
