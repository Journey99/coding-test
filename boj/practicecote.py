from collections import Counter
from collections import deque
import sys
input = sys.stdin.readline

def problem_1205():
    n, new, p = map(int, input().split())
    scores = list(map(int, input().split())) if n > 0 else []

    # n, new, p = 3, 90, 10
    # scores = [100, 90, 80]

    if n == 0:
        print(1)
        exit()

    cnt = 1
    for score in scores:
        if score > new:
            cnt += 1
        else:
            break

    # 랭킹 리스트가 꽉 차지 않은 경우
    if n < p:
        print(cnt)
        exit()

    # 랭킹 리스트가 꽉 찬 경우
    if new > scores[-1]:
        print(cnt)
    else:
        print(-1)

def prblem_1244():
    switch_num = int(input())
    onoff = list(map(int, input().split()))

    stu_num = int(input())

    for _ in range(stu_num):
        sex, num = map(int, input().split())

        if sex == 1:
            k = num
            while k <= switch_num:
                onoff[k-1] ^= 1
                k += num

        else:
            onoff[num-1] ^= 1

            l = num - 2
            r = num 

            while 0 <= l and r < switch_num and onoff[l] == onoff[r]:
                onoff[l] ^= 1
                onoff[r] ^= 1
                l -= 1
                r += 1
                
    for i in range(0, switch_num, 20):
        print(*onoff[i:i+20])

def problem_9017():
    '''
    1. 6명 다 들어왔는지부터 확인 -> n % teams == 0 이면 다 들어온거
    2. 다 들어온 팀만 점수 확인
    3. 점수 확인할 때 5번째 선수의 점수 따로 저장
    '''

    t = int(input())
    for _ in range(t):
        n = int(input())
        teams = list(map(int, input().split()))
        
        # 팀 인원 수 카운트
        counter = Counter(teams)

        # 6명 모두 있는 팀만 추림
        valid = {team for team, c in counter.items() if c == 6}
        
        # 점수 계산 준비
        score = {team: [] for team in valid}
        fifth = {team : None for team in valid}

        rank = 1

        for team in teams:
            if team not in valid:
                # rank += 1
                continue

            if len(score[team]) < 4:
                score[team].append(rank)
            elif fifth[team] is None:
                fifth[team] = rank
            
            rank += 1

        
        answer = None
        best = (float('inf'), float('inf'))

        for team in valid:
            total = sum(score[team])
            f = fifth[team]

            if (total, f) < best:
                best = (total, f)
                answer = team

        print(answer)

def problem_17266():
    n = int(input()) # 굴다리의 길이
    m = int(input()) # 가로등의 개수
    x = list(map(int, input().split())) # 가로등의 위치

    def can_cover(h):
        current_coverd = 0
        for pos in x:
            if pos - h > current_coverd:
                return False
            current_coverd = pos + h
        return current_coverd >= n


    left, right = 1, n
    answer = right

    while left <= right:
        mid = (left + right) // 2

        if not can_cover(mid):
            left = mid + 1
        else:
            answer = mid
            right = mid - 1

    print(answer)            

    '''
    # 다른방식
    max_size = 0
    for i in range(1, m):
        max_size = max(max_size, x[i] - x[i-1])

    max_size = max((max_size+1)//2, x[0], n-x[-1])
    print(max_size)
    '''

def problem_2164():
    n = int(input())
    queue = deque(range(1, n + 1))

    while len(queue) > 1:
        queue.popleft()
        queue.append(queue.popleft())

    print(queue[0])




if __name__ == "__main__":
    # problem_1205()  
    # prblem_1244()
    # problem_9017()
    # problem_17266()
    problem_2164()