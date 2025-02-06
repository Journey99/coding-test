# 유클리드 호제법
'''
- 두 수의 최대 공약수를 효율적으로 구하는 알고리즘
- 두 정수 a,b가 있을 때 a,b의 최대 공약수는 b와 a%b의 최대 공약수와 같다
- b가 a%b의 공약수일 때, a%b == 0 이라면 b가 최대공약수 이다.
'''

def eucild(a, b):
    if b == 0:
        return a
    return eucild(b, a% b)

a, b = map(int, input().split())
if a < b:
    a, b = b, a

print(eucild(a, b))