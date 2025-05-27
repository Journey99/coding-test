# 스토쿠

import sys
input = sys.stdin.readline

sudoku = [list(map(int, input().split())) for _ in range(9)]

# 빈칸 좌표 저장
blanks = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blanks.append((i, j))

# 유효한 숫자 확인
def is_valid(x, y, num):
    # 가로줄
    if num in sudoku[x]:
        return False
    
    # 세로줄
    for i in range(9):
        if num  == sudoku[i][y]:
            return False
        
    # 3x3
    start_x, start_y = 3 * (x//3), 3 * (y//3)
    for i in range(3):
        for j in range(3):
            if sudoku[start_x + i][start_y + j] == num:
                return False
    
    return True

# 백트래킹 함수
def solve(idx):
    if idx == len(blanks):
        for row in sudoku:
            print(' '.join(map(str, row)))
        exit()
    
    x, y = blanks[idx]
    for num in range(1, 10):
        if is_valid(x, y, num):
            sudoku[x][y] = num
            solve(idx + 1)
            sudoku[x][y] = 0 # 아닐시

solve(0)

