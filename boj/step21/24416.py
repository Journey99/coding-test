# 알고리즘 수업 - 피보나치 수 1

def fib_recursive(n):
    if n == 1 or n == 2:
        return 1
    return fib_recursive(n-1) + fib_recursive(n-2)

def fib_dp(n):
    f = [0] * (n+1)
    f[1] = 1
    f[2] = 1

    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]

    return f[n]

n = int(input())

print(fib_dp(n))
print(n-2)  



'''
재귀호출의 경우 코드 실행횟수는 피보나치 수와 같다
-> n==1 or n==2 일때 실행되므로
동적 프로그래밍의 경우 for문이 도는만큼 실행되기 때문에 n-2
'''