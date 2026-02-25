from collections import Counter
import math

def problem_1():
    '''
    딱지놀이
    '''
    n = int(input())

    for _ in range(n):
        a = list(map(int, input().split()))[1:]
        b = list(map(int, input().split()))[1:]

        a_cnt = Counter(a)
        b_cnt = Counter(b)

        flag = False
        for i in [4, 3, 2, 1]:
            if a_cnt[i] > b_cnt[i]:
                print("A")
                flag = True
                break
            elif a_cnt[i] < b_cnt[i]:
                print("B")
                flag = True
                break
        
        if not flag:
            print("D")
    print()

def problem_2():
    '''
    인공지능 청소기
    : 이 문제는 그래프를 이용하는게 아니라 단순 수학문제
    1. 상하좌우로만 움직일 때 도착지까지 가장 빠른 거리는 |x| + |y|
    2. 도착지까지의 최소 거리와 남은 시간의 차이가 짝수여야 갔다왔다를 할 수 있음

    '''
    t = int(input())
    for _ in range(t):
        x, y, n = map(int, input().split())

        min_dist = abs(x) + abs(y)

        if n >= min_dist and (n-min_dist) % 2 == 0:
            print("YES")
        else:
            print("NO")

def problem_3():
    '''
    소금물의 농도 구하기
    print(f"{n / (n+m) * 7:.2f}") : 이렇게 할 경우 print부분에서 반올림을 수행해서 일부 케이스에서 fail의 결과를 가질 수 있음
    '''
    n, m = map(int, input().split())
    # print(f"{n / (n+m) * 7:.2f}")

    salt = n * 0.07
    total = n + m
    result = (salt / total) * 100
    result = math.floor(result * 100) / 100
    print(f"{result:.2f}")

def problem_4():
    '''
    장마
    '''
    n, m = map(int, input().split())
    height = list(map(int, input().split()))

    down_system = set()

    for idx in range(m):
        s, e = map(int, input().split())
        
        for i in range(s-1, e):
            height[i] += 1
            down_system.add(i)

        if (idx + 1) % 3 == 0:
            for i in down_system:
                height[i] -= 1
            
            down_system.clear()

    print(*height)

        


if __name__ == '__main__':
    # problem_1()
    # problem_2()
    # problem_3()
    problem_4()