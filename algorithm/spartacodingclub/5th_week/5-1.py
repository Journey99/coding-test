# 최소 비용으로 도시 여행하기
import heapq
import sys
input = sys.stdin.read

def dijkstra(graph, start, n):
    distances = [float('inf')] * (n + 1)
    distances[start] = 0
 
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

n = int(input())  # 도시의 수
m = int(input())  # 도로의 수
graph = {i: [] for i in range(1, n + 1)}

for i in range(m):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))
    graph[v].append((u, cost))  # 양방향 도로

start, end = map(int, input().split())

distances = dijkstra(graph, start, n)
print(distances[end] if distances[end] != float('inf') else -1)
