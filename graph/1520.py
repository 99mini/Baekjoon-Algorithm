from collections import deque

m, n = map(int, input().split())
#https://www.acmicpc.net/problem/1520
#bfs이용
data = []
for i in range(m):
  data.append(list(map(int, input().split)))

queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue.append((0, 0))
while queue:
  now = queue.popleft()
  for i in range(4):
    nx = 
