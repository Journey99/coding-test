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



if __name__=='__main__':
    problem_1()