import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n,m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

result = 0

def dfs(row,col,visited):
   global isOutside
   visited[row][col] = True
   for i in range(4):
        nrow = row + dx[i]
        ncol = col + dy[i]

        if nrow >= 0 and nrow < n and ncol >=0 and ncol < m:
            if not visited[nrow][ncol]:
                if board[nrow][ncol] == 0:
                    dfs(nrow, ncol, visited) 
        else:
            isOutside = True

def check_outside(row,col,visited,outsides):
   outsides[row][col] = True
   for i in range(4):
        nrow = row + dx[i]
        ncol = col + dy[i]

        if nrow >= 0 and nrow < n and ncol >=0 and ncol < m:
            if not outsides[nrow][ncol]:
                if visited[nrow][ncol]:
                    check_outside(nrow, ncol, visited, outsides) 

def printState():
    print(result)

    print("board")
    print(*board, sep='\n', end='\n\n')
    print("outsides")
    print(*outsides, sep='\n',end='\n\n')
    print("visited")
    print(*visited, sep='\n', end='\n\n')



while sum(sum(b)for b in board):
    result += 1    
    visited = [[False for _ in range(m)]for _ in range(n)]
    outsides = [[False for _ in range(m)]for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0 and not visited[i][j]:
                isOutside = False
                dfs(i,j,visited)
                
                if isOutside:
                    check_outside(i,j,visited,outsides)

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                connected = 0
                for k in range(4):
                    nrow = i + dx[k]
                    ncol = j + dy[k]

                    if nrow >= 0 and nrow < n and ncol >=0 and ncol < m:
                        if outsides[nrow][ncol]:
                            connected += 1
                    else:
                        connected += 1

                if connected >= 2:
                    board[i][j] = 0 

    # printState()

print(result)