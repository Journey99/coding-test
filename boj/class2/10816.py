n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_count = {}
for n in n_list:
    try:
        n_count[n] += 1
    except:
        n_count[n] = 1

answer = []
for m in m_list:
    try:
        answer.append((n_count[m]))
    except:
        answer.append(0)

for i in answer:
    print(i, end= ' ')


"""
from sys import stdin

N = int(input())
arr_n = list(map(int,stdin.readline().split()))
M = int(input())
arr_m = list(map(int,stdin.readline().split()))

dic = dict()

for i in arr_n:
    try :
        dic[i] += 1
    except:
        dic[i] = 1

for i in arr_m:
    try:
        print(dic[i] , end = " ")
    except:
        print(0, end=" ")
    


"""