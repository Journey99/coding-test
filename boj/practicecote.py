'''
https://www.acmicpc.net/workbook/view/8708
'''

from collections import Counter
from collections import deque
import bisect
import heapq
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

def problem_13305():
    n = int(input())
    length = list(map(int, input().split()))
    prices = list(map(int, input().split()))

    min_price = prices[0]
    answer = 0

    for i in range(n-1):
        if prices[i] < min_price:
            min_price = prices[i]
        
        answer += min_price * length[i]

    print(answer)

def problem_20920():
    n, m = map(int, input().split())

    words = {}

    for _ in range(n):
        word = input().strip()
        if len(word) >= m:
            words.setdefault(word, 0)
            words[word] += 1
        
    sorted_items = sorted(
        words.items(),
        key = lambda x: (-x[1], -len(x[0]), x[0])
    )

    for item, key in sorted_items:
        print(item)

def problem_2512():
    n = int(input())
    want = list(map(int, input().split()))
    budget = int(input())

    if sum(want) <= budget:
        print(max(want))
    else:
        want.sort()
        left, right = 0, want[-1] 
        answer = 0

        while left <= right:
            mid = (left + right) // 2

            total = sum(i if i <= mid else mid for i in want)

            if total > budget:
                right = mid - 1
            else:
                left = mid + 1
                answer = mid

        print(answer)

def problem_21921():
    n, x = map(int, input().split())
    visitors = list(map(int, input().split()))

    if sum(visitors) == 0:
        print("SAD")
    else:    
        total = sum(visitors[:x])
        max_num = total
        cnt = 1

        for i in range(n-x):
            total = total - visitors[i] + visitors[x+i]
        
            if max_num < total:
                max_num = total
                cnt = 1
            elif max_num == total:
                cnt += 1

        print(max_num)
        print(cnt)

def problem_1515():
    n = input()

    idx = 0
    num = 1

    while idx < len(n):
        
        for c in str(num):
            if idx < len(n) and c == n[idx]:
                idx += 1
        
        num += 1

    print(num-1)

def problem_19941():
    n, k = map(int, input().split())
    ph = list(input().strip())

    cnt = 0
    for i in range(n):
        if ph[i] == 'P':
                for j in range(i-k, i+k+1):
                    if 0 <= j and j < n and ph[j] == 'H':
                        cnt += 1
                        ph[j] = 'X'
                        break

    print(cnt)

def problem_17484():
    n, m = map(int, input().split())
    fuels = []

    for _ in range(n):
        fuels.append(list(map(int, input().split())))

    '''
    dp[d][n][m] : d방향일 때

    d = 0 : 왼쪽으로 , d = 1 : 아래로, d = 2 : 오른쪽으로 
    '''

    INF = 10**9
    dp = [[[INF] * m for _ in range(n)] for _ in range(3)]

    for k in range(3):
        for j in range(m):
            dp[k][0][j] = fuels[0][j]


    for i in range(1, n):
        for j in range(m):
            if j+1 < m: # 왼쪽아래방향으로 온 경우
                dp[0][i][j] = min(dp[1][i-1][j+1], dp[2][i-1][j+1]) + fuels[i][j]
                
            # 바로아래방향으로 온 경우
            dp[1][i][j] = min(dp[0][i-1][j], dp[2][i-1][j]) + fuels[i][j]

            if j - 1 >= 0: # 오른쪽아래방향으로 온 경우
                dp[2][i][j] = min(dp[0][i-1][j-1], dp[1][i-1][j-1]) + fuels[i][j]

        
    answer = INF
    for j in range(m):
        for d in range(3):
            answer = min(dp[d][n-1][j], answer)

    print(answer)

def problem_2607():

    n = int(input().strip())
    standard = input().strip()

    words = [input().strip() for _ in range(n-1)]

    answer = 0
    standard_cnt = Counter(standard)

    for word in words:
        if abs(len(standard) - len(word)) > 1:
            continue

        word_cnt = Counter(word)

        diff = sum(
            abs(standard_cnt[c] - word_cnt[c])
            for c in set(standard_cnt) | set(word_cnt)
        )

        if diff <= 2:
            answer += 1

    print(answer)

def problem_3758():
    T = int(input())

    for _ in range(T):
        teams = {}
        n, k, t, m = map(int, input().split())
        
        for time in range(m):
            team, probelm, score = map(int, input().split())

            if team not in teams:
                teams[team] = {
                    "scores" : [0] * k,
                    "total" : 0,
                    "submit_cnt" : 0,
                    "last_time" : 0
                }
            
            info = teams[team]

            info["submit_cnt"] += 1
            info["last_time"] = time

            old = info["scores"][probelm-1]
            if score > old:
                info["scores"][probelm-1] = score
                info["total"] += (score - old)


        ranked = sorted(teams.items(), key=lambda x: (-x[1]["total"], x[1]["submit_cnt"], x[1]["last_time"]))
        
        for rank, (team_id, _) in enumerate(ranked, 1):
            if team_id == t:
                print(rank)
                break

def problem_20310():
    s = input()

    num0 = s.count("0")
    num1 = s.count("1")

    remove0 = num0 // 2
    remove1 = num1 // 2

    result = []

    for ch in s:
        if ch == "1" and remove1 > 0:
            remove1 -= 1
        else:
            result.append(ch)

    final = []
    for ch in reversed(result):
        if ch == "0" and remove0 > 0:
            remove0 -= 1
        else:
            final.append(ch)

    final.reverse()

    print("".join(final))

def problem_19637():
    n, m = map(int, input().split())

    titles = []
    limits = []

    for _ in range(n):
        name, num = input().split()
        titles.append(name)
        limits.append(int(num))

    for _ in range(m):
        power = int(input())
        idx = bisect.bisect_left(limits, power)
        print(titles[idx])

def problem_22233():
    n, m = map(int, input().split())
    memo = set()

    for _ in range(n):
        memo.add(input().strip())

    for _ in range(m):
        keywords = input().strip().split(',')
        
        for keyword in keywords[:10]:
            if keyword in memo:
                memo.remove(keyword)

        print(len(memo))

def problem_1927():

    n = int(input())
    pq = []

    for _ in range(n):
        x = int(input())

        if x == 0:
            if pq:
                p = heapq.heappop(pq)
                print(p)
            else:
                print(0)
        else:
            heapq.heappush(pq, x)
    
def problem_20006():
    p, m = map(int, input().split())

    rooms = [] # 각 방: {"base": 기준레벨, "players": [(level, name), ...]}

    for _ in range(p):
        l, n = input().split()
        l = int(l)

        entered = False

        for room in rooms:
            if len(room["players"]) < m and room["base"] - 10 <= l <= room["base"] + 10:
                room["players"].append((l, n))
                entered = True
                break

        if not entered:
            rooms.append({
                "base": l,
                "players": [(l, n)]
            })
        
    for room in rooms:
        if len(room["players"]) == m:
            print("Started!")
        else:
            print("Waiting!")

        room["players"].sort(key=lambda x: x[1])

        for level, name in room["players"]:
            print(level, name)
        
def problem_11501():
    t = int(input())

    for _ in range(t):
        n = int(input())
        stocks = list(map(int, input().split()))

        max_price = 0
        benefit = 0

        for i in range(n-1, -1, -1):
            stock = stocks[i]
            if max_price < stock:
                max_price = stock
            
            else: # max_price > stock
                benefit += max_price - stock
        
        print(benefit)

def problem_1406():

    left = list(input().rstrip())
    right = []

    m = int(input())

    for _ in range(m):
        command = input().split()

        if command[0] == 'L':
            if left:
                right.append(left.pop())
        elif command[0] == 'D':
            if right:
                left.append(right.pop())

        elif command[0] == 'B':
            if left:
                left.pop()
        else:
            left.append(command[1])


    print(''.join(left + right[::-1]))

def problem_2304():
    n = int(input())
    info = []

    for _ in range(n):
        l, h = map(int, input().split())
        info.append((l, h))

    info.sort(key=lambda x: x[0])
    max_idx = max(range(n), key=lambda i: info[i][1])

    area = 0

    # 왼쪽
    cur_max = 0
    for i in range(0, max_idx):
        cur_max = max(cur_max, info[i][1])
        width = info[i+1][0] - info[i][0]
        area += cur_max * width

    # 오른쪽
    cur_max = 0
    for i in range(n-1, max_idx, -1):
        cur_max = max(cur_max, info[i][1])
        width = info[i][0] - info[i-1][0]
        area += cur_max * width

    # 최대높이 기둥 면적
    area += info[max_idx][1]

    print(area)

def problem_2075():
    n = int(input())

    pq = []
    for _ in range(n):
        nums = map(int, input().split())

        for num in nums:
            if len(pq) < n:
                heapq.heappush(pq, num)
            else:
                if num > pq[0]:
                    heapq.heappop(pq)
                    heapq.heappush(pq, num)

    print(heapq.heappop(pq))

def problem_1138():
    n = int(input())
    info = list(map(int, input().split()))
    result = []

    for height in range(n, 0, -1):
        result.insert(info[height-1], height)
    
    print(*result)
        
def problem_1260():
    
    def dfs(graph, v, visited):
        visited[v] = True
        print(v, end=' ')

        for nxt in graph[v]:
            if not visited[nxt]:
                dfs(graph, nxt, visited)

    def bfs(graph, v, visited):
        visited[v] = True
        pq = deque([v])


        while pq:
            now = pq.popleft()
            print(now, end=' ')

            for nxt in graph[now]:
                if not visited[nxt]:
                    visited[nxt] = True
                    pq.append(nxt)


    n, m, v = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    for g in graph:
        g.sort()


    visited_dfs = [False] * (n+1)
    visited_bfs = [False] * (n+1)

    dfs(graph, v, visited_dfs)
    print()
    bfs(graph, v, visited_bfs)

def problem_14940():
    n, m = map(int, input().split())

    matrix = []
    dist = [[-1] * m for _ in range(n)]

    start_x, start_y = -1, -1

    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

        for j in range(m):
            if row[j] == 2:
                start_x, start_y = i, j


    dist[start_x][start_y] = 0
    queue = deque([(start_x, start_y)])
    moves = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        now_x, now_y = queue.popleft()

        for x, y in moves:
            nx, ny = now_x + x, now_y + y

            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[now_x][now_y] + 1
                queue.append((nx, ny))


    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                print(0, end=' ')
            else:
                print(dist[i][j], end=' ')
        print()

def problem_20922():
    '''
    투포인터 사용해서 해결
    '''

    n, k = map(int, input().split())
    s = list(map(int, input().split()))

    answer = 0
    cnt = {}
    left = 0

    for right in range(n):
        value = s[right]
        cnt[value] = cnt.get(value, 0) + 1

        if cnt[value] > k:
            while cnt[value] > k:
                cnt[s[left]] -= 1
                left += 1
        
        answer = max(answer, right-left+1)

    print(answer)

    

if __name__ == "__main__":
    # problem_1205()  
    # prblem_1244()
    # problem_9017()
    # problem_17266()
    # problem_2164()
    # problem_13305()
    # problem_20920()
    # problem_2512()
    # problem_21921()
    # problem_1515()
    # problem_19941()
    # problem_17484()
    # problem_2607()
    # problem_3758()
    # problem_20310()
    # problem_19637()
    # problem_22233()
    # problem_1927()
    # problem_20006()
    # problem_11501()
    # problem_1406()
    # problem_2304()
    # problem_2075()
    # problem_1138()
    # problem_1260()
    # problem_14940()
    problem_20922()