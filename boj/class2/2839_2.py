# 설탕 배달

def main(x):

    if x % 5 == 0:
        return int(x/5)

    else:
        answer = 0
        while True:

            x -= 3
            if x < 0:
                return -1

            answer += 1

            if x % 5 == 0:
                answer += x/5
                return int(answer)


n = int(input())
print(main(n))

