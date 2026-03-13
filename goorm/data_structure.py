import heapq
import sys
input = sys.stdin.readline

def problem_1():
    '''
    [0커플]
    - 점수를 합한 값이 0이 되는 두 명을 짝지어서 소개팅
    - n점을 가진 사람이 항상 존재한다는 규칙을 지키지 못해 두사람이 소개팅을 받지 못함
    - 소개팅을 받지 못한 두 사람의 점수를 합한 값을 출력
    '''

    n = int(input()) # 지인의 수
    score = list(map(int, input().split()))
    score.sort()
    st = []

    for i in score:
        if st and st[-1] + i == 0:
            st.pop()
        else:
            st.append(i)
    print(sum(st))

def problem_2():
    '''
    [블록 게임]
    - (0,0) 위치에 점수가 1인 블록을 놓음
    - 상하좌우로 블록을 놓음
    - 이미 블록이 있는 경우 새로 놓을 위치에 원래 블록이 존재하지 않을 때까지 최근에 놓은 블록들을 순서대로 제거
    '''

    n = int(input())
    directioin = input()
    scores = list(map(int, input().split()))

    x, y = 0, 0
    history = [(0,0)] # 좌표 스택
    block_score = [1]
    visited = {(0,0)}

    for i in range(n):
        d = directioin[i]
        s = scores[i]

        if d == 'R': x += 1
        elif d == 'L': x -= 1
        elif d == 'U': y += 1
        elif d == 'D': y -= 1        

        if (x, y) in visited:
            while history:
                px, pv = history.pop()
                block_score.pop()
                visited.remove((px, pv))

                if (px, pv) == (x,y):
                    break
        
        history.append((x,y))
        block_score.append(s)
        visited.add((x,y))


    print(sum(block_score)) 
            

def problem_3():
    '''
    [ADAS 시스템]
    '''

    w, h = map(int, input().split())
    maps = [list(input().strip()) for _ in range(w)]

    sx, sy = 0, 0
    for i in range(w):
        for j in range(h):
            if maps[i][j] == 'S':
                sx, sy = i, j
                break

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 주변 8방향 (위험도 계산용)
    nx8 = [-1, -1, -1, 0, 0, 1, 1, 1]
    ny8 = [-1, 0, 1, -1, 1, -1, 0, 1]

    def get_risk(x, y):
        if maps[x][y] == 'S':
            return 0
        
        risk = 0
        # 주변 8칸의 P 개수 확인
        for i in range(8):
            nx, ny = x + nx8[i], y + ny8[i]
            if 0 <= nx < w and 0 <= ny < h:
                if maps[nx][ny] == 'P':
                    risk += 1
        
        # 현재 칸이 P라면 추가로 +5점 (보통의 칸은 주변 P 개수만큼만)
        if maps[x][y] == 'P':
            risk += 5
        return risk

    # 3. 우선순위 큐를 이용한 시뮬레이션
    pq = []
    heapq.heappush(pq, (0, sx, sy))
    visited = [[False] * h for _ in range(w)]
    total_score = 0

    while pq:
        current_risk, x, y = heapq.heappop(pq)
        
        if visited[x][y]:
            continue
        
        visited[x][y] = True
        # 시작 지점이 아닐 때만 점수 합산
        if maps[x][y] != 'S':
            total_score += current_risk
        
        # 도착지 E에 도달하면 즉시 종료
        if maps[x][y] == 'E':
            break
        
        # 상, 하, 좌, 우 순서로 후보지 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < w and 0 <= ny < h and not visited[nx][ny]:
                # 다음 칸의 위험도를 미리 계산하여 큐에 삽입
                next_risk = get_risk(nx, ny)
                heapq.heappush(pq, (next_risk, nx, ny))

    print(max(0, total_score))


    

        









if __name__=='__main__':
    # problem_1()
    # problem_2()
    problem_3()