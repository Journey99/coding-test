# 체스판 다시 칠하기 2

'''
1. 입력 받아서 보드 저장
2. W 시작, B 시작 기준으로 오류 배열 만들기 (0/1)
3. 각각에 대해 2차원 누적합 배열 만들기
4. 슬라이딩 윈도우로 K×K 영역 훑으며 틀린 칸 수 비교
5. 전체 중 최소값 출력
'''

import sys
input = sys.stdin.readline

# 1
n, m, k = map(int, input().split())
board = [input().strip() for _ in range(n)]

# 2
diff_w = [[0] * m for _ in range(n)] # w로 시작하는
diff_b = [[0] * m for _ in range(n)] # b로 시작하는

## (i + j) % 2를 이용해서 흰색/검정 기준 판단
for i in range(n):
    for j in range(m):
        expected_w = 'W' if (i + j) % 2 == 0 else 'B'  # W 시작 체스판
        expected_b = 'B' if (i + j) % 2 == 0 else 'W'  # B 시작 체스판
        if board[i][j] != expected_w:
            diff_w[i][j] = 1
        if board[i][j] != expected_b:
            diff_b[i][j] = 1

# 3
def build_prefix(diff):
    prefix = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            prefix[i][j] = (
                prefix[i - 1][j]
                + prefix[i][j - 1]
                - prefix[i - 1][j - 1]
                + diff[i - 1][j - 1]
            )
    return prefix    

prefix_w = build_prefix(diff_w)
prefix_b = build_prefix(diff_b)

# 4
min_change = float('inf')

for i in range(k, n+1): # 행 시작점 : i-k+1
    for j in range(k, m+1): # 열 시작점 : j-k+1
        total_w = (
            prefix_w[i][j]
            - prefix_w[i - k][j]
            - prefix_w[i][j - k]
            + prefix_w[i - k][j - k]
        )
        total_b = (
            prefix_b[i][j]
            - prefix_b[i - k][j]
            - prefix_b[i][j - k]
            + prefix_b[i - k][j - k]
        )
        # 최소 칠해야 하는 횟수
        min_change = min(min_change, total_w, total_b)

print(min_change)       