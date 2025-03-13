# 수 정렬하기3

'''
아래와 같이 코드를 작성하면 메모리 초과 발생
- sort, sorted 사용
- for문 안에 append 사용
'''
import sys

n = int(input())
result = []

for _ in range(n):
    result.append(int(sys.stdin.readline()))

result.sort()
for i in result:
    print(i)


'''
메모리 초과 발생을 해결하기 위해 아래와 같이 코드 작성
- 계수정렬을 이용한다
- 미리 공간을 할당한다
'''

import sys

n = int(sys.stdin.readline())
arr = [0] * (10000+1)

for _ in range(n):
    arr[int(sys.stdin.readline())] += 1

for i in range(len(arr)):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)