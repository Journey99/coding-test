# 설탕 배달
'''
1. 5로 나눠질 경우
2. 5와 3의 조합으로 나눠 담을 수 있는 경우
3. 3으로 나눠질 경우
4. 둘다 나눠지지 않을 경우
'''

n = int(input())
result = []

if n % 5 == 0:
    print(n//5)
else:
    cnt = 0
    while n > 0:
        n -= 3
        cnt += 1
        if n % 5 == 0:
            cnt += n // 5
            print(cnt)
            break
        elif n == 1 or n == 2:
            print(-1)
            break
        elif n == 0:
            print(cnt)
            break


## 조금 더 간단한 코드
while True:
    if n % 5 == 0:
        cnt += n // 5
        print(cnt)
        break
    n -= 3
    cnt += 1

    if n < 0:
        print(n-1)
        break