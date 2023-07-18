# TODO 빙산
from collections import deque
import sys

input = sys.stdin.readline

def search(r,c):
    dq = deque([(r,c)])
    while dq:
        row, col = dq.popleft()
        for dr,dc in zip([0,0,1,-1],[1,-1,0,0]):
            nr = dr + row
            nc = dc + col
            if nr >= 0 and nr < n and nc >= 0 and nc < m:
                if graph[nr][nc] == 0:
                    melting.append((row,col))
                elif not visited[nr][nc] and graph[nr][nc] > 0:
                    visited[nr][nc] = 1
                    dq.append((nr,nc))

time = -1
mass = 0

n,m = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

while True:
    mass = 0
    visited = [[0]*m for _ in range(n)]
    melting = []
    
    time += 1

    for row in range(n):
        for col in range(m):
            if not visited[row][col] and graph[row][col]:
                visited[row][col] = 1
                search(row,col)
                mass += 1

    for melt in melting:
        if graph[melt[0]][melt[1]] > 0:
            graph[melt[0]][melt[1]] -= 1

print(time)