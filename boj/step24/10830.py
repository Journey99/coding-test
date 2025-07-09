# 행렬 제곱
'''
- 구해야 하는 것 : A^B % 1000
- b가 크기 때문에 단순 반복은 불가능 -> 분할 정복 사용
- 행렬 곱셈 함수를 만들고 곱셈 후에는 MOD 1000 을 적용해야 함
'''

import sys
input = sys.stdin.readline

n, b = map(int, input().split())
mod = 1000

a = [list(map(int, input().split())) for _ in range(n)]

# 행렬 곱셈 함수
def mat_mul(x, y):
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += x[i][k] * y[k][j]
            result[i][j] %= mod

    return result


# 분할 정복으로 a^b 구하기
def mat_pow(matrix, power):
    if power == 1:
        return [[elem % mod for elem in row] for row in matrix]
    
    temp = mat_pow(matrix, power // 2)
    if power % 2 == 0:
        return mat_mul(temp, temp)
    else: # 홀수 일 때
        return mat_mul(mat_mul(temp, temp), matrix)

result = mat_pow(a, b)

for row in result:
    print(*row)
    