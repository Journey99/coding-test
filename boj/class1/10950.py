#T = int(input())
#for i in range(T):
#    a, b = map(int, input().split())
#    print(a+b)
# 위에 처럼 하면 입력받으면 합을 출력하는 과정 T번 반복
T = int(input())
result = []
for i in range(T):
    a, b = map(int, input().split())
    result.append(a + b)

for j in result:
    print(j)
