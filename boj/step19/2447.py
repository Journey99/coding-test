# 별 찍기 - 10

def draw_star(x, y, size):
    if size == 1:
        board[x][y] = '*'
        return
    
    w = size // 3
    for dx in range(3):
        for dy in range(3):
            if dx == 1 and dy == 1:
                continue
            draw_star(x+dx *w, y + dy*w, w)
    

n = int(input())
board = [[' ' for _ in range(n)] for _ in range(n)]
draw_star(0, 0, n)

for row in board:
    print("".join(row))