import sys
from collections import deque

input = sys.stdin.readline

n,k,r = map(int,input().split())

graph = {}
for _ in range(r):
    start_row, start_col, end_row, end_col = map(int,input().split())
    if not (start_row,start_col) in graph:
        graph[(start_row,start_col)] = [(end_row, end_col)]
    else:
        graph[(start_row,start_col)].append((end_row, end_col))
    if not (end_row, end_col) in graph:
        graph[(end_row,end_col)] = [(start_row, start_col)]
    else:
        graph[(end_row,end_col)].append((start_row, start_col))


cows = [tuple(map(int,input().split())) for _ in range(k)]

count = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def bfs(init_row,init_col):
    q = deque()
    q.append((init_row,init_col))
    visited[init_row][init_col] = True
    while q:
        row, col = q.popleft()
        for i in range(4):
            nr = row + dx[i]
            nc = col + dy[i]

            if nr <= n and nr >= 1 and nc <= n and nc >= 1 and not visited[nr][nc]:
                if (row,col) in graph and (nr,nc) in graph[(row,col)]:
                    continue

                visited[nr][nc] = True
                q.append((nr,nc))

for i,cow in enumerate(cows):
    visited = [[True if i == 0 or j == 0 else False for i in range(n+1) ] for j in range(n+1)]
    bfs(cow[0], cow[1])
    for c in cows[i+1:]:
        if not visited[c[0]][c[1]]:
            count += 1

print(count)