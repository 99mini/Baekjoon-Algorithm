from collections import deque
import sys

input = sys.stdin.readline
F, S, G, U, D = map(int,input().split())

graph:dict[int,list] = {}

for i in range(1,F+1):
    graph[i] = []
    if i + U <= F: 
        graph[i].append(i+U)
    if i - D > 0:
        graph[i].append(i-D)

visited = [-1] * (F+1)
dq = deque()

def bfs(start,target):
    dq.append(start)
    visited[start] = 0

    while dq:
        current = dq.popleft()
        if current == target:
            return
        for node in graph[current]:
            if visited[node] == -1:
                dq.append(node)
                visited[node] = visited[current] + 1

bfs(S,G)
print('use the stairs' if visited[G] == -1 else visited[G])