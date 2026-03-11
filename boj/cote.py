'''
https://www.acmicpc.net/workbook/view/4349

'''

import sys
input = sys.stdin.readline


def problem_12865():
    '''
    dp[i][w]
    - i : 현재 고려하고 있는 물건의 번호
    - w : 배낭의 현재 남은 무게 한도
    - dp[i][w] : i번째까지 고려했을 때, 무게 합이 k를 넘지 않으면서 얻을 수 있는 가치의 최댓값
    '''

    n, k = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(n)]

    dp = [0] * (k+1)

    for w, v in info:
        for j in range(k, w-1, -1):
            dp[j] = max(dp[j], v+dp[j-w])

    print(dp[k])


if __name__ == '__main__':
    problem_12865()