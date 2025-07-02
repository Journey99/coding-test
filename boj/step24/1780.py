# 종이의 개수
import sys
input = sys.stdin.readline

n = int(input())
papers = [list(map(int, input().split())) for _ in range(n)]
minus, zero, one = 0, 0, 0

def count_num(x, y, size):
    global minus, zero, one
    start = papers[x][y]

    for i in range(x, x+size):
        for j in range(y, y+size):
            if start != papers[i][j]:
                third = size // 3
                count_num(x, y, third)
                count_num(x + third, y, third)
                count_num(x + 2* third, y, third)
                count_num(x, y + third, third)
                count_num(x, y + 2 * third, third)
                count_num(x + third, y + third, third)
                count_num(x + 2 * third, y + third, third)
                count_num(x + third, y + 2*third, third)
                count_num(x + 2*third, y + 2*third, third)
                return


    if start == -1:
        minus += 1
    elif start == 0:
        zero += 1
    else:
        one += 1

count_num(0, 0, n)
print(minus)
print(zero)
print(one)