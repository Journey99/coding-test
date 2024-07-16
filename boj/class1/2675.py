# 문자열 반복

t = int(input())  # 텍스트의 개수 입력받기
for i in range(t):
    r, string = input().split()
    r = int(r)

    for ch in string:
        for j in range(r):
            print(ch, end='')    # end를 사용하면 그 뒤의 출력값과 이어서 출력한다

    print()