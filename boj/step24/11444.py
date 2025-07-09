# 피보나치 수 6
'''
이 문제에서는 n이 매우 큰 수가 될 수 있다.
따라서 동적계획법이나 재귀는 시간이나 공간을 따졌을 때 비효율적일 수 있다
'''
mod = 1_000_000_007

n = int(input())

def mat_mul(x, y):
    n = len(x)
    z = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                z[i][j] += x[i][k] * y[k][j]
            
            z[i][j] %= mod

    return z

def mat_pow(matrix, power):
    if power == 1:
        return [[elem % mod for elem in row] for row in matrix]
    
    temp = mat_pow(matrix, power // 2)
    if power % 2 == 0:
        return mat_mul(temp, temp)
    else:
        return mat_mul(mat_mul(temp, temp), matrix)
    

m = [[1, 1], [1, 0]]
print(mat_pow(m, n)[0][1])