#https://www.acmicpc.net/problem/2630
#quadTree
n = int(input())
data = []
for _ in range(n):
  data.append(list(map(int, input().split())))
result = [0,0]

def quadTree(size, row, col, color):
  if size == 0:
    return
  check = True
  for i in range(row, row+size):
    if not check:
      break
    for j in range(col,col+size):
      if data[i][j] == color:
        pass
      else:
        check = False
        break
  if check:
    result[color] += 1
    return

  quadTree(size//2,row,col,color)
  quadTree(size//2,row,col+size//2,color)
  quadTree(size//2,row+size//2,col,color)
  quadTree(size//2,row+size//2,col+size//2,color) 

quadTree(n,0,0,0)
quadTree(n,0,0,1)
for r in result:
  print(r)
