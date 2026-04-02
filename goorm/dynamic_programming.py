import sys
input = sys.stdin.readline

def problem_1():
    '''
    [통증(2)]
    - 통증 수치가 높다면 게임에서 승리하기 어려우므로, 아이템을 적절히 사용해 통증 수치를 0으로 유지
    - 통증 수치를 감소시켜 주는 아이템 2가지 : bandage, medicine
    - 각 아이템을 사용시 A, B 만큼 통증 수치를 감소시켜 준다
    - 플레이어가 통증 수치를 0으로 줄이기 위해 필요한 아이템의 최소 개수를 구하라.
    - 단, 사용했을 때 수치가 0보다 작아지는 아이템은 사용할 수 없음
    '''

    n = int(input())
    a, b = map(int, input().split())

    answer = float('inf')

    for a_cnt in range(n // a + 1):
        remain = n - a * a_cnt

        if remain % b == 0:
            b_cnt = remain // b
            answer = min(answer, a_cnt + b_cnt)

    if answer == float('inf'):
        print(-1)
    else:
        print(answer)


    ### dp를 이용한 방법
    N = int(input())
    A, B = map(int, input().split())

    INF = 10**9
    dp = [INF] * (N + 1)
    dp[0] = 0

    for i in range(1, N + 1):
        if i - A >= 0:
            dp[i] = min(dp[i], dp[i - A] + 1)
        if i - B >= 0:
            dp[i] = min(dp[i], dp[i - B] + 1)

    print(dp[N] if dp[N] != INF else -1)

def problem_2():
    '''
    [최대 쇼핑몰 구역 찾기]
    - 건물의 배치는 2차원 행렬로 표현
    - 각 셀은 건물의 유무
    - 쇼핑몰은 비어있는 공간의 정사각형 영역 내에만 지을 수 있음
    - 여러 건물이 있는 2차원 행렬에서 만들 수 있는 가장 큰 정사각형의 넓이는?
    '''

    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    dp = [[0] * m for _ in range(n)]
    max_size = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(
                        dp[i-1][j],
                        dp[i][j-1],
                        dp[i-1][j-1]
                    ) + 1

                max_size = max(max_size, dp[i][j])

    print(max_size * max_size)





if __name__=='__main__':
    # problem_1()
    problem_2()