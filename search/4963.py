while True:
  w, h  = map(int, input().split())
  if w == 0 and h == 0:
    break
  
  island = [list(map(int, input().split())) for i in range(h)]
  visted = [[0 for i in range(w)] for j in range(h)]
  cnt = 0
  dx = [0,0,1,-1,1,1,-1,-1]
  dy = [1,-1,0,0,1,-1,1,-1]

  def dfs(x,y):
    visted[x][y] = 1

    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx >= h or nx < 0 or ny >= w or ny < 0:
        continue
      if island[nx][ny] == 1 and visted[nx][ny] == 0:
        dfs(nx,ny)

  for i in range(h):
    for j in range(w):
      if island[i][j] == 1 and visted[i][j] == 0:
        dfs(i,j)
        cnt += 1
  print(cnt)
