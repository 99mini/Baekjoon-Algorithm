# 플로이드-와샬 알고리즘
# https://www.acmicpc.net/problem/11403
INF = 123456789

n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
  tmp = list(map(int, input().split()))
  for j in range(n):
    if tmp[j] == 1:
      matrix[i][j] = 1
    else:
      matrix[i][j] = INF

for k in range(n):
  for a in range(n):
    for b in range(n):
      matrix[a][b] = min(matrix[a][b], matrix[a][k]+matrix[k][b])
      
for row in matrix:
  for r in row:
    if r != INF:
      print(1, end=' ')
    else:
      print(0, end=' ')
  print()
