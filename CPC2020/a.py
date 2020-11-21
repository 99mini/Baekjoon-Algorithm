n, k = map(int, input().split())

grid = []
for _ in range(n):
  grid.append(list(map(int, input().split())))

result = []

for row in grid:
  
  for _ in range(k):
    tmp = []
    for col in row:
      for _ in range(k):
        tmp.append(col)
    result.append(tmp)    

for i in range(n*k):
  for j in range(n*k):
    print(result[i][j], end=' ')
  print('')
