import sys
from collections import deque

input = sys.stdin.readline

def bfs(start,colors):
    q.append(start)
    colors[start] = 1

    while q:
        currentNode = q.popleft()
        if colors[currentNode] == 1:
            color = 2
        else:
            color = 1

        for nextNode in graph[currentNode]:
            if colors[nextNode] == 0:
                colors[nextNode] = color
                q.append(nextNode)
            else:
                if colors[nextNode] == colors[currentNode]:
                    return False
    return True

t = int(input())
for _ in range(t):
    n,m = map(int,input().split())

    graph = {i:[] for i in range(1,n+1)}
    colors = [0 for _ in range(n+1)]

    q = deque()

    for _ in range(m):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)

    res = False
    for i in range(1,n+1):
        if colors[i] == 0:
            res = bfs(i,colors)
            if not res: break

    if res:
        print('possible')
    else:
        print('impossible')

    
    