# 최소공배수
import sys

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

t = int(input())
result = []

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    lcm = a * b // gcd(a,b)    
    result.append(lcm)

for r in result:
    print(r)



'''
[최대공약수]
유클리드 호제법 : 두 정수가 n과m이고, n을 m으로 나눈 나머지가 r일 때, n과 m의 최대공약수는 m과 r의 최대공약수와 같다
=> gcd(n,m) = gcd(m,r) = gcd(m, n%m)

[최소공배수]
n = gcd x a, m = gcd x b
lcm = gcd x a x b
    = n x m / gcd

'''