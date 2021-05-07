# 브르투포스 알고리즘 이용 - 완전탐색 알고리즘
# 가능한 모든 경우의 수를 모두 탐색하는 방법!
N = int(input())
result = 0
for i in range(1, N+1):
    a = list(map(int,str(i)))
    s = i + sum(a)
    if( s== N):
        result = i
        break

print(result)