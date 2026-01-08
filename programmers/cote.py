from collections import deque, defaultdict
from math import ceil
import heapq


def problem_1(info, n, m):
    '''
    완전범죄
    https://school.programmers.co.kr/learn/courses/30/lessons/389480
    '''

    dp = [[False] * m for _ in range(n)]
    dp[0][0] = True

    for a_trace, b_trace in info:
        new_dp = [[False] * m for _ in range(n)]

        for a in range(n):
            for b in range(m):
                if not dp[a][b]:
                    continue

                # a가 훔치는 경우
                na = a + a_trace
                if na < n:
                    new_dp[na][b] = True

                # b가 훔치는 경우
                nb = b + b_trace
                if nb < m:
                    new_dp[a][nb] = True

        dp = new_dp

    for a in range(n):
        for b in range(m):
            if dp[a][b]:
                return a
    
    return -1

def problem_2(players, m, k):
    '''
    서버 증설 횟수
    https://school.programmers.co.kr/learn/courses/30/lessons/389479?language=python3
    '''
    servers = deque()
    cnt = 0
    over = 0

    for p in players:
        # 기존 서버 나이 증가시키고, 만료되는 서버 개수 집계
        if servers:
            for i in range(len(servers)):
                servers[i] += 1
                if servers[i] >= k:
                    over += 1
            
            # 만료 서버 제거
            if over > 0:
                for _ in range(over):
                    servers.popleft()
                
                over = 0
        
        need = p // m

        if need > 0 and need > len(servers):
            for _ in range(need - len(servers)):
                servers.append(0)
                cnt += 1

    return cnt

if __name__ == '__main__':
    # problem_1()
    # problem_2([0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5], 3, 5)