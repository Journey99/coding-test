# 나이순 정렬

n = int(input())

li = []
for _ in range(n):
    age, name = input().split()
    li.append([int(age), name])     # 2차원 리스트로 저장

li.sort(key=lambda x: int(x[0]))      # sort()함수를 이용하여 오름차순정렬 lambda함수를 이용하여 첫번째 요소에 대해서만 정렬

for i in li:
    print(i[0], i[1])