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
    


if __name__ == "__main__":
    # problem_1205()  
    prblem_1244()