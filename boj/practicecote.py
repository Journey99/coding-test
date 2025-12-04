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


if __name__ == "__main__":
    problem_1205()  