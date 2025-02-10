# 직사각형에서 탈출

x, y, w, h = list(map(int, input().split()))
print(min(x, y, w -x, h -y))