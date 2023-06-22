import sys

input = sys.stdin.readline

n = int(input())
classroom = []
possible = [[0 for _ in range(n)] for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

result = 0

for _ in range(n):
    classroom.append(list(map(str, input().split())))

def search(row,col):
    global result
    for i in range(4):
        nrow = row + dx[i]
        ncol = col + dy[i]
        line_row = nrow
        line_col = ncol

        while line_row >= 0 and line_row < n and line_col >= 0 and line_col < n:
            if classroom[nrow][ncol] == 'T':
                return False
            if classroom[line_row][line_col] == 'T':
                while line_row != nrow or line_col != ncol:
                    line_row -= dx[i]
                    line_col -= dy[i]
                    possible[line_row][line_col] += 1
                    if possible[line_row][line_col] == 2:
                        result -=1
                result += 1
                break
            elif classroom[line_row][line_col] == 'S':
                break
            else:
                line_row += dx[i]
                line_col += dy[i]

    return True
        
for i in range(n):
    for j in range(n):
        if classroom[i][j] == 'S':
            if not search(i,j):
                print('NO')
                exit()

if result <= 3:
    print('YES')
else:
    print('NO')