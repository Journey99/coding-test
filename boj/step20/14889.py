# 스타트와 링크
import sys
input = sys.stdin.readline

n = int(input())
power = [list(map(int, input().split())) for _ in range(n)]

# 방문한 사람 체크 (True면 start팀, False면 link팀)
visited = [False] * n

min_diff = float('inf')

# 팀 능력치 계산 함수
def team_score(team):
    score = 0
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            a = team[i]
            b = team[j]
            score += power[a][b] + power[b][a]
    return score

# 팀 나누기 (백트래킹)
def dfs(depth, idx):
    global min_diff

    # start 팀이 n//2명이 되면 link 팀도 자동 결정됨
    if depth == n // 2:
        start_team = []
        link_team = []

        for i in range(n):
            if visited[i]:
                start_team.append(i)
            else:
                link_team.append(i)

        start_score = team_score(start_team)
        link_score = team_score(link_team)
        diff = abs(start_score - link_score)

        min_diff = min(min_diff, diff)
        return

    # 조합 만들기 (idx부터 시작)
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i + 1)
            visited[i] = False

dfs(0, 0)
print(min_diff)
