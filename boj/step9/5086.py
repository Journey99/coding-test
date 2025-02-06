# 배수와 약수
'''
1. 첫 번째 숫자가 두 번째 숫자의 약수라면 factor
2. 첫 번째 숫자가 두 번째 숫자의 배수라면 multiple
3. 약수와 배수 둘다 아니라면 neither
'''

while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break

    if b % a == 0:
        print("factor")
    elif a % b == 0:
        print("multiple")
    else:
        print("neither")