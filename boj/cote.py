'''
https://www.acmicpc.net/workbook/view/4349

'''
import heapq
import sys
input = sys.stdin.readline


def problem_12865():
    '''
    dp[i]
    - 가방이 최대 i만큼의 무게를 담을 수 있을 때, 가질 수 있는 최대 가치
    '''

    n, k = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(n)]

    dp = [0] * (k+1)

    for w, v in info:
        for j in range(k, w-1, -1):
            dp[j] = max(dp[j], v+dp[j-w])

    print(dp[k])

def problem_11401():
    MOD = 1_000_000_007

    n, k = map(int, input().split())

    # 1. n!까지의 팩토리얼을 미리 계산
    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % MOD  # 항상 MOD로 나눠주기

    # 2. 모듈러 역원 함수: 페르마의 소정리 이용
    def modinv(a):
        return pow(a, MOD - 2, MOD)
        # pow(a, b, c)는 (a^b) % c 를 빠르게 계산해주는 파이썬 내장함수

    # 3. 이항계수 계산: n! * (k!)^-1 * ((n-k)!)^-1 mod MOD
    result = fact[n]
    result = result * modinv(fact[k]) % MOD
    result = result * modinv(fact[n - k]) % MOD

    print(result)

def problem_10830():
    n, b = map(int, input().split())
    mod = 1000

    a = [list(map(int, input().split())) for _ in range(n)]

    # 행렬 곱셈 함수
    def mat_mul(x, y):
        result = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    result[i][j] += x[i][k] * y[k][j]
                result[i][j] %= mod

        return result


    # 분할 정복으로 a^b 구하기
    def mat_pow(matrix, power):
        if power == 1:
            return [[elem % mod for elem in row] for row in matrix]
        
        temp = mat_pow(matrix, power // 2)
        if power % 2 == 0:
            return mat_mul(temp, temp)
        else: # 홀수 일 때
            return mat_mul(mat_mul(temp, temp), matrix)

    result = mat_pow(a, b)

    for row in result:
        print(*row)

def problem_1655():
    '''
    정수를 하나씩 외칠때마다 중간값 말하기
    -> 최대 힙과 최소 힙을 동시에 사용하기
    : 두 힙의 크기 차이가 1보다 커지지 않아야 한다 -> 최대 힙의 top이 중간값이 됨
      최대 힙의 루트는 항상 최소 힙의 루트보다 작거나 같아야 함
    

    '''
    n = int(input())
    left_q = []
    right_q = []

    for _ in range(n):
        num = int(input())

        # 삽입
        if len(left_q) == len(right_q):
            heapq.heappush(left_q, -num)
        else:
            heapq.heappush(right_q, num)
        
        # 값의 역전 현상 체크
        if right_q and -left_q[0] > right_q[0]:
            left_max = -heapq.heappop(left_q)
            right_min = heapq.heappop(right_q)

            heapq.heappush(left_q, -right_min)
            heapq.heappush(right_q, left_max)
        
        print(-left_q[0])



if __name__ == '__main__':
    # problem_12865()
    # problem_11401()
    # problem_10830()
    problem_1655()