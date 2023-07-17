import sys

input = sys.stdin.readline

n = int(input())
a,b = map(int,input().split())
m = int(input())
family = {i:[] for i in range(1,n+1)}
for _ in range(m):
    x,y = map(int,input().split())

    family[x].append(y)
    family[y].append(x)

def dfs(start, target):   
    current = stack.pop()
    if current == target:
        return
    for node in family[current]:
        if visited[node] == -1:
            stack.append(node)
            visited[node] = visited[current] + 1
            dfs(start,target)

stack = []
stack.append(a)
visited = [-1 for _ in range(n+1)]
visited[a] = 0
count = 0
dfs(a,b)
print(visited[b])