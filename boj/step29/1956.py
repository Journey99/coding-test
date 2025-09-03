# 운동
'''
사이클이 존재하는 경우
dist[i][i] 가 무한대가 아닐 경우
dist[i][i] < 0 : 음수 사이클 존재
'''


def floyd_warshall(n, edges):
    dist = [[float('inf')] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        dist[i][i] = 0
    
    for a, b, c in edges:
        dist[a][b] = min(dist[a][b], c)
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    

    return dist

v, e = map(int, input().split())
edges = []

for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

result = floyd_warshall(v, edges)

answer = float('inf')
for i in range(1, v+1):
    for j in range(1, v+1):
        if i != j:
            if result[i][j] != float('inf') and result[j][i] != float('inf'):
                answer = min(answer, result[i][j] + result[j][i])


print(answer if answer != float('inf') else -1)