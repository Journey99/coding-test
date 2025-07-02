# 색종이 만들기
'''
핵심 아이디어
- 보고있는 정사각형이 모두 같은 색이면 그만
- 아니라면 4개로 분할해서 재귀적으로 반복

분할 : 4개의 정사각형으로 나눔
정복 : 한가지 색으로만 채워졌는지 확인 / 그렇지 않으면 분할
통합 : 개수를 합쳐서 계산
'''

import sys
input = sys.stdin.readline

n = int(input())
square = [list(map(int, input().split())) for _ in range(n)]
white, blue = 0, 0


def count_color(x, y, size):
    global white, blue
    color = square[x][y]

    # 전체 영역이 같은지 확인
    for i in range(x, x+size):
        for j in range(y, y+size):
            if square[i][j] != color:
                half = size // 2
                count_color(x, y, half)
                count_color(x, y+half, half)
                count_color(x+half, y, half)
                count_color(x+half, y+half, half)
                return
    
    if color == 0:
        white += 1
    else:
        blue +=1


count_color(0,0,n)
print(white)
print(blue)