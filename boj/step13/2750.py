# 수 정렬하기

n = int(input())
result = []
for _ in range(n):
    result.append(int(input()))

result = sorted(result)
for i in result:
    print(i)
