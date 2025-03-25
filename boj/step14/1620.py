# 나는야 포켓몬 마스터 이다솜
import sys

n, m = map(int, sys.stdin.readline().split())

poketmons_num = {}  
poketmons_name = {}  

for i in range(1, n + 1):
    name = sys.stdin.readline().strip()  
    poketmons_num[i] = name
    poketmons_name[name] = i  

for _ in range(m):
    problem = sys.stdin.readline().strip()
    
    if problem.isdigit(): 
        print(poketmons_num[int(problem)])  
    else:  
        print(poketmons_name[problem]) 