# 쿼드트리
import sys
input = sys.stdin.readline

n = int(input())
video = [list(map(int, input().strip())) for _ in range(n)]

def quadtree(x, y, size):
    start = video[x][y]
    same = True

    for i in range(x, x+size):
        for j in range(y, y+size):
            if video[i][j] != start:
                same = False
                break
        if not same:
            break
    
    if same:
        return str(start)

    half = size // 2
    return '(' + \
            quadtree(x, y, half) + \
            quadtree(x, y+half, half) + \
            quadtree(x+half, y, half) + \
            quadtree(x+half, y+half, half) + \
            ')'
 
print(quadtree(0, 0, n))

'''



'''