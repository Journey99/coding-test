'''
https://www.acmicpc.net/workbook/view/8708
'''

from collections import Counter
from collections import deque
from collections import defaultdict
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

def problem_1446():
    n, d = map(int, input().split())

    shortcuts = [[] for _ in range(d+1)]
    for _ in range(n):
        s, e, c = map(int, input().split())
        if e > d:
            continue
        if c >= (e - s):
            continue

        shortcuts[s].append((e, c))


    # dp[x] = x까지 가는 최소 거리
    dp = [i for i in range(d+1)]

    for i in range(d+1):
        if i > 0:
            dp[i] = min(dp[i], dp[i-1] + 1)
        
        for end, cost in shortcuts[i]:
            dp[end] = min(dp[end], dp[i] + cost) # i = starts

    print(dp[d])

def problem_17615():
    n = int(input())
    balls = list(input().strip())

    def cnt_move(color, direction):
        '''
        r을 왼쪽으로 몰기
        r을 오른쪽으로 몰기
        b를 왼쪽으로 몰기
        b를 오른쪽으로 몰기
        중에 최소 이동 횟수를 골라야 함

        이미 붙어 있는 덩어리는 움직임 대상 x
        '''

        conti = 0
        if direction == 'left':
            for ball in balls:
                if ball == color:
                    conti += 1
                else:
                    break
            
        else: # right
            for ball in reversed(balls):
                if ball == color:
                    conti += 1
                else:
                    break
        
        return balls.count(color) - conti

    result = min(
        cnt_move('R', 'left'),
        cnt_move('R', 'right'),
        cnt_move('B', 'left'),
        cnt_move('B', 'right')
    )

    print(result)

def problem_2531():
    n, d, k, c = map(int, input().split())


    sushi = [int(input()) for _ in range(n)]

    counter = Counter(sushi[:k])
    answer = len(counter) + (1 if c not in counter else 0)

    for i in range(1, n):
        # 왼쪽 제거
        left = sushi[i-1]
        counter[left] -= 1
        if counter[left] == 0:
            del counter[left]
        
        # 오른쪽 추가
        right = sushi[(i+k-1) % n]
        counter[right] += 1

        cnt = len(counter) + (1 if c not in counter else 0)
        answer = max(cnt, answer)

    print(answer)

def problem_1522():
    s = input()

    '''
    1. 문자열에서 a의 총 개수를 센다
    2. 길이가 "a개수" 인 구간을 원형으로 슬라이딩하면서 그 구간 안에 b개수를 센다
    3. 그중 최솟값이 정답
    '''
    a_cnt = s.count('a') 

    new_s = s + s
    b_cnt = new_s[:a_cnt].count('b')
    answer = b_cnt

    for i in range(1, len(new_s)):
        if new_s[i-1] == 'b':
            b_cnt -= 1
        if new_s[(i+a_cnt-1) % len(new_s)] == 'b':
            b_cnt += 1
        
        answer = min(answer, b_cnt)

    print(answer)

def problem_1697():
    n, k = map(int, input().split())

    MAX = 100000
    visited = [-1] * (MAX + 1)

    queue = deque([n])
    visited[n] = 0

    while queue:
        x = queue.popleft()

        if x == k:
            print(visited[x])
            break

        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= MAX and visited[nx] == -1:
                visited[nx] = visited[x] + 1
                queue.append(nx)

def problem_1283():
    '''
    왼쪽 -> 오른쪽 순서로 단축키로 지정되었는지 확인 -> 안되어있으면 지정
    이미 다 지정되어 잇으면 -> 왼쪽부터 차례대로 알파벳을 보면서 단축키로 지정 
    어떤것도 지정안되면 그냥 놔두기

    '''
    n = int(input())
    used = set()

    for _ in range(n):
        line = input().rstrip()
        words = line.split()

        # 단축키 위치
        shortcut_pos = -1

        # 1. 각 단어 첫 글자
        word_pos = []
        pos = 0
        for word in words:
            word_pos.app(pos)
            pos += len(word) + 1. # 단어 + 공백

        for i, word in enumerate(words):
            first = word[0].lower()
            if first.isalpha() and first not in used:
                used.add(first)
                shortcut_pos = word_pos[i]
                break

        
        # 2. 왼쪽부터 모든 글자
        if shortcut_pos == -1:
            for i, ch in enumerate(line):
                if ch.isalpha() and ch.lower not in used:
                    used.add(ch.lower())
                    shortcut_pos = i
                    break

        
        if shortcut_pos != -1:
            result = line[:shortcut_pos] + '[' + line[shortcut_pos] + ']' + line[shortcut_pos+1:]
        else:
            result = line

        print(result)

def problem_15989():
    t = int(input())
    MAX = 10000

    dp = [0] * (MAX + 1)
    dp[0] = 1

    for num in (1,2,3):
        for i in range(num, MAX+1):
            dp[i] += dp[i-num]

    for _ in range(t):
        n = int(input())
        print(dp[n])

def problem_13549():
    n, k = map(int, input().split())
    MAX = 100000

    dist = [-1] * (MAX + 1)
    queue = deque([n])
    dist[n] = 0

    while queue:
        x = queue.popleft()

        if x == k:
            print(dist[k])
            break

        nx = x * 2
        if 0 <= nx <= MAX and dist[nx] == -1:
            dist[nx] = dist[x]
            queue.appendleft(nx)

        
        for nx in (x-1, x+1):
            if 0 <= nx <= MAX and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                queue.append(nx)

def problem_12919():
    '''
    t에서 s를 만들 수 있는지로 푼다.
    1. t의 마지막 문자가 a -> a 제거
    2. t의 마지막 문자가 b -> 맨앞 b 제거 후 뒤집기
    '''

    s = input().strip()
    t = input().strip()

    def dfs(t, s):
        if t == s:
            return True
        if len(t) < len(s):
            return False
        
        if t[-1] == 'A':
            if dfs(t[:-1], s):
                return True
        
        if t[0] == 'B':
            new_t = t[1:][::-1]
            if dfs(new_t, s):
                return True
        
        return False


    if dfs(t, s):
        print(1)
    else:
        print(0)

def problem_16928():
    n, m = map(int, input().split())
    lader, snake = {}, {}

    for _ in range(n):
        x, y = map(int, input().split())
        lader[x] = y

    for _ in range(m):
        x, y = map(int, input().split())
        snake[x] = y

    visitied = [False] * 101
    dice = [1, 2, 3, 4, 5, 6]

    queue = deque()
    queue.append((1, 0)) # 첫번째 칸, 횟수
    visitied[1] = True

    while queue:
        x, cnt = queue.popleft()

        if x == 100:
            print(cnt)
            exit(0)

        for d in dice:
            nx = x + d
            if 0 < nx <= 100 and not visitied[nx]:
                if nx in lader:
                    nx = lader[nx]
                elif nx in snake:
                    nx = snake[nx]
                
                if not visitied[nx]:
                    queue.append((nx, cnt+1))
                    visitied[nx] = True

def problem_20055():
    n, k = map(int, input().split())
    belt = deque(map(int, input().split()))
    robots = deque([False] * n)

    step = 0

    while True:
        step += 1

        belt.rotate(1)
        robots.rotate(1)
        robots[-1] = False

        for i in range(n-2, -1, -1):
            if robots[i] and not robots[i+1] and belt[i+1] > 0:
                robots[i] = False
                robots[i+1] = True
                belt[i+1] -= 1

        robots[-1] = False

        # 로봇 올리기
        if belt[0] > 0:
            robots[0] = True
            belt[0] -= 1

        if belt.count(0) >= k:
            print(step)
            break

def problem_20437():
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())

        pos = defaultdict(list)

        for i, ch in enumerate(s):
            pos[ch].append(i)

        min_len = float('inf')
        max_len = 0

        for ch in pos:
            if len(pos[ch]) < k:
                continue

            for i in range(len(pos[ch]) - k + 1):
                length = pos[ch][i+k-1] - pos[ch][i] + 1
                min_len = min(min_len, length)
                max_len = max(max_len, length)

        if min_len == float('inf'):
            print(-1)
        else:
            print(min_len, max_len)

def problem_2493():
    n = int(input())
    tops = list(map(int, input().split()))

    stack = []

    for i, t in enumerate(tops):
        
        # 나보다 낮은 탑들은 의미 없으므로 제거
        while stack and stack[-1][0] < t:
            stack.pop()
        
        if stack:
            print(stack[-1][1] + 1, end=' ')
        else:
            print(0, end=' ')
        
        stack.append((t, i))

def problem_14719():
    h, w = map(int, input().split())
    blocks = list(map(int, input().split()))

    l, r = 0, w-1
    left_max, right_max = 0, 0
    total = 0

    while l < r:
        if blocks[l] < blocks[r]:
            if blocks[l] >= left_max:
                left_max = blocks[l]
            else:
                total += left_max - blocks[l]
            l += 1
        else:
            if blocks[r] >= right_max:
                right_max = blocks[r]
            else:
                total += right_max - blocks[r]
            r -= 1

    print(total)

    '''
    # 스택 사용한 코드
    stack = []
    total = 0

    for i in range(w):
        while stack and blocks[stack[-1]] < blocks[i]:
            bottom = stack.pop()

            if not stack:
                break

            left = stack[-1]
            height = min(blocks[left], blocks[i]) - blocks[bottom]
            width = i - left - 1

            total += height * width

        stack.append(i)
    
    print(total)
    '''

def problem_5972():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b, w = map(int, input().split())
        graph[a].append((b, w))
        graph[b].append((a, w))

    start = 1
    distance = [float('inf')] * (n+1)
    distance[start] = 0

    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for nxt, w in graph[now]:
            cost = dist + w
            if cost < distance[nxt]:
                distance[nxt] = cost
                heapq.heappush(heap, (cost, nxt))

    print(distance[n])

def problem_2467():
    n = int(input())
    liquid = list(map(int, input().split()))

    l, r = 0, len(liquid) - 1
    result_l, result_r = 0, 0

    min_value = float('inf')

    while l < r:
        s = liquid[l] + liquid[r]

        if abs(s) < min_value:
            min_value = abs(s)
            result_l, result_r = liquid[l], liquid[r]
        
        if s < 0:
            l += 1
        else:
            r -= 1

    print(result_l, result_r)

def problem_7682():
    '''
    말 개수 규칙 : x의 개수 = o의 개수 + 1 또는 x의 개수 = o의 개수 
    승리 상태 체크 : 가로, 세로, 대각선 -> 승부가 안날 수도 있음
    승리자와 말 개수 일치 여부
        - x가 이기면 : x = o + 1
        - o가 이기면 : o = x + 1

    1. 개수 틀리면 -> 무조건 invalid
    2. x, o 빙고 둘 다면 -> invalid
    3. x 빙고면 -> x == o + 1 이어야 valid
    4. o 빙고면 -> o == x + 1 이어야 valid
    5. 빙고 없으면 -> 개수 맞으면 valid
    '''

    def isbingo(xo, check):
        lines = [
            (0,1,2), (3,4,5), (6,7,8),   # 가로
            (0,3,6), (1,4,7), (2,5,8),   # 세로
            (0,4,8), (2,4,6)             # 대각선
        ]

        for a, b, c in lines:
            if xo[a] == xo[b] == xo[c] == check:
                return True
        return False


    while True:
        xo = input()
        if xo == 'end':
            break

        x_cnt = xo.count('X')
        o_cnt = xo.count('O')
        # 말 개수 규칙
        if x_cnt == o_cnt + 1 or x_cnt == o_cnt:
            x_bingo = isbingo(xo, 'X')
            o_bingo = isbingo(xo, 'O')

            # 1. x, o 둘다 빙고 일때
            if x_bingo and o_bingo:
                print("invalid")
            # 2. x가 빙고 일때
            elif x_bingo:
                if x_cnt == o_cnt + 1:
                    print("valid")
                else:
                    print("invalid")
            # 3. o가 빙고 일때
            elif o_bingo:
                if x_cnt == o_cnt:
                    print("valid")
                else:
                    print("invalid")
            # 4. 빙고 없을 때
            else:
                if x_cnt + o_cnt == 9:
                    print("valid")
                else:
                    print("invalid")
        else:
            print("invalid")

def problem_2668():
    '''
    dfs를 이용해서 푸는 문제
    출발한 숫자 집합 == 도착한 숫자 집합
    -> 자기 자신으로 되돌아오는 사이클 구조로 사이클에 속한 노드들이 정답
    '''

    n = int(input())
    arr = [0] + [int(input()) for _ in range(n)]
    visited = [False] * (n+1)
    answer = []

    def dfs(start, current, path):
        visited[current] = True
        nxt = arr[current]
        path.append(current)

        if not visited[nxt]:
            dfs(start, nxt, path)
        else:
            if nxt in path:
                idx = path.index(nxt)
                for x in path[idx:]:
                    answer.append(x)
        path.pop()

        return

    for i in range(1, n+1):
        if not visited[i]:
            dfs(i, i, [])

    answer.sort()
    print(len(answer))
    for a in answer:
        print(a)
    
def problem_22251():
    '''
    현재 숫자 x를 기준으로 세그먼트 led를 최대 p개까지 반전해서 1~n 이하의 다른 숫자 몇개 만들 수 있는지

    0~9 -> 7세그먼트 on/off 상태
    cost[a][b] = a -> b로 바꾸는 데 필요한 led 반전 수

    1. 세그먼트 비트 정의
    2. cost[10][10] 전처리
    3. x를 k자리 문자열로 변환
    4. 1부터 n까지 k자리 문자열로 변환해서 자리별 cost 합산
    '''
    
    n, k, p, x = map(int, input().split()) # n : n층 / k : 자리수 / p : 변환 최대 수
    answer = 0

    segment = [
        [1,1,1,0,1,1,1],  # 0
        [0,0,1,0,0,1,0],  # 1
        [1,0,1,1,1,0,1],  # 2
        [1,0,1,1,0,1,1],  # 3
        [0,1,1,1,0,1,0],  # 4
        [1,1,0,1,0,1,1],  # 5
        [1,1,0,1,1,1,1],  # 6
        [1,0,1,0,0,1,0],  # 7
        [1,1,1,1,1,1,1],  # 8
        [1,1,1,1,0,1,1],  # 9    
    ]

    cost = [[0] * 10 for _ in range(10)]

    for a in range(10):
        for b in range(10):
            if a != b:
                for i in range(7):
                    if segment[a][i] != segment[b][i]:
                        cost[a][b] += 1

    x_str = str(x).zfill(k)

    for y in range(1, n+1):
        total = 0
        y_str = str(y).zfill(k)

        for i in range(k):
            total += cost[int(x_str[i])][int(y_str[i])]
        
        if 0 < total <= p:
            answer += 1

    print(answer)

def problem_7490():
    
    def dfs(num, expr):
        if num == n:
            if eval(expr.replace(' ', '')) == 0:
                result.append(expr)
            return
        
        dfs(num + 1, expr + ' ' + str(num + 1))
        dfs(num + 1, expr + '+' + str(num + 1))
        dfs(num + 1, expr + '-' + str(num + 1))

    t = int(input())
    for _ in range(t):
        n = int(input())
        result = []

        dfs(1, '1')

        result.sort()
        for r in result:
            print(r)
        print()

def problem_16234():
    
    def bfs(i, j):
        queue = deque([(i, j)])
        union = [(i, j)]
        visited[i][j] = True
        population_sum = graph[i][j]
        
        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    if L <= abs(graph[nx][ny] - graph[x][y]) <= R:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        union.append((nx, ny))
                        population_sum += graph[nx][ny]
        
        return population_sum, union


    N, L, R = map(int, input().split())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    day = 0
    while True:
        visited = [[False] * N for _ in range(N)]
        flag = False # 인구 이동이 발생했는지

        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    population_sum, union = bfs(i, j, N, L, R)
                    if len(union) >= 2:
                        new = population_sum // len(union)
                        for x, y in union:
                            graph[x][y] = new
                        flag = True
        
        if flag == False:
            break
        day += 1

    print(day)

def problem_2138():
    n = int(input())
    start = input().strip()
    end = input().strip()

    def toggle(arr, idx):
        for i in (idx-1, idx, idx+1):
            if 0 <= i < n:
                arr[i] = '1' if arr[i] == '0' else '0'

    def solve(first_on):
        arr = list(start)
        cnt = 0

        if first_on: # 첫번째 스위치 누름
            toggle(arr, 0)
            cnt += 1
        
        for i in range(1, n):
            if arr[i-1] != end[i-1]:
                toggle(arr, i)
                cnt += 1

        if ''.join(arr) == end:
            return cnt
        else:
            return float('inf')

    ans = min(solve(True), solve(False))
    print(ans if ans != float('inf') else -1)

def problem_1863():
    n = int(input())
    stack = []
    answer = 0

    for _ in range(n):
        x, h = map(int, input().split())

        while stack and stack[-1] > h:
            if stack[-1] != 0:
                answer += 1
            stack.pop()
        
        if not stack or stack[-1] < h:
            stack.append(h)
        
    while stack:
        if stack[-1] != 0:
            answer += 1
        stack.pop()

    print(answer)

def problem_4485():

    def dijkstra(graph, n):
        distance = [[float('inf')] * n for _ in range(n)]
        distance[0][0] = graph[0][0]
        queue = [(graph[0][0], 0, 0)]
        while queue:
            dist, nowx, nowy = heapq.heappop(queue)
            
            if distance[nowx][nowy] < dist:
                continue

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = nowx + dx
                ny = nowy + dy
                if 0 <= nx < n and 0 <= ny < n:
                    cost = dist + graph[nx][ny]
                    if cost < distance[nx][ny]:
                        distance[nx][ny] = cost
                        heapq.heappush(queue, (cost, nx, ny))
        
        return distance[n-1][n-1]


    cnt = 0
    while True:
        n = int(input())
        if n == 0:
            break
        
        cnt += 1
        graph = [list(map(int, input().split())) for _ in range(n)]

        dist = dijkstra(0, 0, graph, n)
        print(f"Problem {cnt}: {dist}")
        
def problem_1253():
    '''
    음수도 가능하기 때문에 자기자신을 제외하고 모든 수를 확인해봐야 함
    '''
    n = int(input())
    ls = list(map(int, input().split()))
    ls.sort()

    answer = 0
    for i in range(n):
        target = ls[i]
        l, r = 0, n-1

        while l < r:
            if l == i:
                l += 1
                continue
            if r == i:
                r -= 1
                continue

            s = ls[l] + ls[r]

            if s == target:
                answer += 1
                break
            elif s < target:
                l += 1
            else:
                r -= 1

    print(answer)

def problem_1806():
    n, s = map(int, input().split())
    ls = list(map(int, input().split()))
    
    current_sum = ls[0]
    l, r = 0, 0
    min_len = float('inf')

    while l < n and r < n:
        if current_sum < s:
            r += 1
            if r < n:
                current_sum += ls[r]
        else:
            min_len = min(min_len, r - l + 1)
            current_sum -= ls[l]
            l += 1

    print(0 if min_len == float('inf') else min_len)

def problem_1987():
    '''
    알파벳 : 26개 -> ord(alpha)
    '''

    def dfs(x, y, cnt):
        global max_len
        max_len = max(max_len, cnt)

        for dx, dy in direction:
            nx = dx + x
            ny = dy + y

            if 0 <= nx < r and 0 <= ny < c:
                idx = ord(graph[nx][ny]) - 65
                if not visitied[idx]:
                    visitied[idx] = True
                    dfs(nx, ny, cnt + 1)
                    visitied[idx] = False

    r, c = map(int, input().split())
    graph = [list(input().strip()) for _ in range(r)]

    visitied = [False] * 26
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_len = 0

                    
    start_idx = ord(graph[0][0]) - 65
    visitied[start_idx] = True
    dfs(0, 0, 1)

    print(max_len)

def problem_2110():
    n, c = map(int, input().split())
    cords = sorted([int(input()) for _ in range(n)])

    def can_install(distance):
        cnt = 1
        location = cords[0] # 공유기 처음 놓는 위치

        for i in range(1, n):
            if cords[i] - location >= distance:
                cnt += 1
                location = cords[i] # 놓는 위치 갱신
        
        return cnt >= c

    # 이분 탐색 범위
    start = 1
    end = cords[-1] - cords[0]
    result = 0

    while start <= end:
        mid = (start + end) // 2

        if can_install(mid):
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    print(result)

def problem_9935():
    s = input()
    bomb = input()

    stack = []
    bomb_len = len(bomb)

    for ch in s:
        stack.append(ch)

        if ch == bomb[-1] and len(stack) >= bomb_len:
            if ''.join(stack[-bomb_len:]) == bomb:
                for _ in range(bomb_len):
                    stack.pop()

    result = ''.join(stack)
    print(result if result else "FRULA")

def problem_13144():
    n = int(input())
    ls = list(map(int, input().split()))

    visited = [False] * 100001
    l = 0
    answer = 0

    for r in range(n):
        while visited[ls[r]]:
            visited[ls[l]] = False
            l += 1
        
        visited[ls[r]] = True
        answer += (r - l + 1)

    print(answer)

def problem_1976():
    n = int(input())
    m = int(input())

    # graph = [[] for _ in range(n+1)]

    # for i in range(1, n+1):
    #     connect = list(map(int, input().split()))
    #     for idx, c in enumerate(connect):
    #         if c == 1:
    #             graph[i].append(idx + 1)

    # plan = list(map(int, input().split()))

    parent = [i for i in range(n + 1)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    # 연결 정보 입력받으며 바로 union
    for i in range(1, n + 1):
        connect = list(map(int, input().split()))
        for j, c in enumerate(connect):
            if c == 1:
                union(i, j + 1) # i번 도시와 j+1번 도시 연결

    plan = list(map(int, input().split()))

    root = find(plan[0])
    is_possible = True
    for i in range(1, m):
        if find(plan[i]) != root:
            is_possible = False
            break

    print("YES" if is_possible else "NO")

def problem_1027():

    def calc_slope(x1, y1, x2, y2):
        return (y2-y1) / (x2-x1)

    n = int(input())
    buildings = list(map(int, input().split()))

    answer = 0
    for i in range(n):
        cnt = 0

        max_slope = -float('inf')
        for j in range(i+1, n):
            slope = calc_slope(i, buildings[i], j, buildings[j])
            if max_slope < slope:
                max_slope = slope
                cnt += 1
        
        min_slope = float('inf')
        for j in range(i-1, -1, -1):
            slope = calc_slope(j, buildings[j], i, buildings[i])
            if min_slope > slope:
                min_slope = slope
                cnt += 1
        
        answer = max(answer, cnt)

    print(answer)

def problem_2179():
    '''
    비슷한 단어
    : n개의 영단어들이 있을 때, 가장 비슷한 두 단어 구해내기
    -> 공통 접두사가 길다는 것은 단어들을 사전적으로 정렬했을 때 서로 가까이 붙어 있다는 뜻!
    -> 인접한 두 단어끼리만 공통 접두사 길이를 구하면 됨 -> 인접하지 않은 단어들 사이의 공통 접두사는 그 사이에 있는 단어들의 접두사보다 길 수 없기 때문!
    '''

    n = int(input())
    ls = []

    for i in range(n):
        ls.append((input().strip(), i))

    sorted_ls = sorted(ls)

    max_len = 0
    lcp = [0] * n # 인접한 단어와 가질 수 있는 최대 접두사 길이

    def get_length(w1, w2):
        cnt = 0
        for a, b in zip(w1, w2):
            if a == b: 
                cnt += 1
            else: 
                break
        return cnt

    for i in range(n-1):
        w1, idx1 = sorted_ls[i]
        w2, idx2 = sorted_ls[i+1]

        length = get_length(w1, w2)
        max_len = max(max_len, length)

        lcp[idx1] = max(lcp[idx1], length)
        lcp[idx2] = max(lcp[idx2], length)
        
    for i in range(n):
        if lcp[i] == max_len:
            s_word = ls[i][0]
            print(s_word)

            for j in range(i+1, n):
                if lcp[j] == max_len and get_length(s_word, ls[j][0]) == max_len:
                    print(ls[j][0])
                    exit()

def problem_2631():
    n = int(input())
    children = [int(input()) for _ in range(n)]

    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if children[j] < children[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    lis_length = max(dp)
    print(n-lis_length)

def problem_4179():
    r, c = map(int, input().split())
    miro = [list(input().strip()) for _ in range(r)]

    fire_q = deque()
    jihun_q = deque()
    fire_time = [[-1] * c for _ in range(r)]
    jihun_time = [[-1] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if miro[i][j] == 'F':
                fire_q.append((i, j))
                fire_time[i][j] = 0
            elif miro[i][j] == 'J':
                jihun_q.append((i, j))
                jihun_time[i][j] = 0

    dx = [-1, 1, 0 ,0]
    dy = [0, 0, -1, 1]

    # 불이 번지는 시간
    while fire_q:
        x, y = fire_q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if miro[nx][ny] != '#' and fire_time[nx][ny] == -1:
                    fire_time[nx][ny] = fire_time[x][y] + 1
                    fire_q.append((nx, ny))

    can = False

    while jihun_q:
        x, y = jihun_q.popleft()

        if x == 0 or x == r-1 or y == 0 or y == c-1:
            print(jihun_time[x][y] + 1)
            can = True
            break
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if miro[nx][ny] != '#' and jihun_time[nx][ny] == -1:
                    if fire_time[nx][ny] == -1 or jihun_time[x][y] + 1 < fire_time[nx][ny]:
                        jihun_time[nx][ny] = jihun_time[x][y] + 1
                        jihun_q.append((nx, ny))

    if not can:
        print("IMPOSSIBLE")

def problem_1238():
    n, m, x = map(int, input().split())

    graph = [[] for _ in range(n+1)] # x -> 집
    reverse_graph = [[] for _ in range(n+1)] # 집 -> x

    for _ in range(m):
        s, e, t = map(int, input().split())
        graph[s].append((e, t))
        reverse_graph[e].append((s, t))

    def dijkstra(start, graph):
        dist = [float('inf')] * (n+1)
        dist[start] = 0
        q = [(0, start)]

        while q:
            d, now = heapq.heappop(q)

            if dist[now] < d:
                continue
            for nxt, w in graph[now]:
                cost = d + w
                if cost < dist[nxt]:
                    dist[nxt] = cost
                    heapq.heappush(q, (cost, nxt))
        return dist

    to_party = dijkstra(x, reverse_graph)
    from_party = dijkstra(x, graph)

    answer = 0
    for i in range(1, n+1):
        answer = max(answer, to_party[i] + from_party[i])

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
    # problem_20922()
    # problem_1446()
    # problem_17615()
    # problem_2531()
    # problem_1522()
    # problem_1697()
    # problem_1283()
    # problem_15989()
    # problem_13549()
    # problem_12919()
    # problem_20437()
    # problem_2493()
    # problem_14719()
    # problem_5972()
    # problem_2467()
    # problem_7682()
    # problem_2668()
    # problem_22251()
    # problem_7490()
    # problem_16234()
    # problem_2138()
    # problem_1863()
    # problem_4485()
    # problem_1253()
    # problem_1806()
    # problem_1987()
    # problem_2110()
    # problem_9935()
    # problem_13144()
    # problem_1976()
    # problem_1027()
    # problem_2179()
    # problem_2631()
    # problem_4179()
    problem_1238()