import sys
import heapq

input = sys.stdin.readline

n,k = map(int,input().split())

matrix = [list(map(int,input().split())) for _ in range(n)]

visited = [[False for _ in range(n)]for _ in range(n)]
distances = [[sys.maxsize for _ in range(n)] for _ in range(n)]

hq = []

def dijkstra(start, distances, visited):
    distances[start] = 0
    heapq.heappush(hq,(start,0))
    visited[start] = True

    while hq:
        current, distance = heapq.heappop(hq)
        visited[current] = True

        if distances[current] < distance:
            continue

        for idx, arr in enumerate(matrix):
            next_node = idx
            next_distance = distance + arr[current]

            if next_distance < distances[idx]:
                distances[idx] = next_distance
                heapq.heappush(hq,(next_node, next_distance))

result = 0

for i in range(n):
    dijkstra(i, distances[i], visited[i])

print(*distances,sep='\n')

for j in range(n):
    if j == k:
        continue
    min_distance = sys.maxsize
    for i in range(n):
        if distances[i][j] == 0:
            continue
        min_distance = min(distances[i][j], min_distance)
    result += min_distance

print(result)




