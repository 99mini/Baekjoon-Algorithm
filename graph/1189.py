import sys

input = sys.stdin.readline

r,c,K = map(int,input().split())

matrix = [list(map(str,input().strip())) for _ in range(r)]

result = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(row,col,k):
    global result

    if k == K: 
        if row == 0 and col == c - 1:
            result += 1            
    else:
        for i in range(4):
            nrow, ncol = row + dx[i], col + dy[i]
            if nrow >= 0 and nrow < r  and ncol >= 0 and ncol < c:
                if matrix[nrow][ncol] != 'T':
                    matrix[nrow][ncol] = 'T'
                    dfs(nrow, ncol,k+1)
                    matrix[nrow][ncol] = '.'

matrix[r-1][0] = 'T'
dfs(r-1,0,1)
print(result)