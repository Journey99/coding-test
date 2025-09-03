# 플로이드
import sys
input = sys.stdin.readline

def floyd_warshall(n, edges):
    dist = [[float('inf')] * (n+1) for _ in range(n+1)]
    
    # 자기자신 초기화
    for i in range(n+1):
        dist[i][i] = 0

    # 정보 저장
    for a, b, c in edges:
        dist[a][b] = min(dist[a][b], c)
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist
    

n = int(input())
m = int(input())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

result = floyd_warshall(n, edges)

for i in range(1, n+1):
    for j in range(1, n+1):
        if result[i][j] == float('inf'):  # 갈 수 없는 경우
            print(0, end=" ")
        else:
            print(result[i][j], end=" ")
    print()
    
    
