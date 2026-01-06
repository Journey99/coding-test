from collections import deque
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




if __name__ == '__main__':
    # problem_1()