import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n,m,r = map(int,input().split())

graph = {i+1:[] for i in range(n)}

visited = [0 for _ in range(n+1)]

k = 1

for _ in range(m):
    u,v = map(int,input().split()) 
    graph[u].append(v)
    graph[v].append(u)

for node in graph:
    graph[node].sort()

def dfs(start):
    global k
    visited[start] = k
    
    for node in graph[start]:
        if not visited[node]:
            k += 1
            dfs(node)

dfs(r)

print(*visited[1:],sep='\n')