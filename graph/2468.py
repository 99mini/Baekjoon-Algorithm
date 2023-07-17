import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def search(row,col,height):
    for dr,dc in zip([0,0,1,-1],[1,-1,0,0]):
        nr = dr + row
        nc = dc + col
        if nr >= 0 and nr < n and nc >= 0 and nc < n:
            if not visited[nr][nc] and height < graph[nr][nc]:
                visited[nr][nc] = 1
                search(nr,nc,height)
            
max_height = -1
result = 1

graph = []

n = int(input())
for _ in range(n):
    rows = list(map(int,input().split()))
    graph.append(rows)
    max_height = max(rows+[max_height])

for height in range(1,max_height):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    count = 0
    for row in range(n):
        for col in range(n):
            if not visited[row][col] and height < graph[row][col]:
                count += 1
                visited[row][col] = 1
                search(row,col,height)

    result = max(count, result)

print(result)