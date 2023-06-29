import sys
import copy

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
games = [list(map(int,input().split())) for _ in range(n)]

# r l d u
dx = [0,0,1,-1]
dy = [1,-1,0,0]

result = - 1

# TODO 2 2 2 2 인 경우 0 0 4 4 만들기
def move(games,row,col, direction):

    if direction == 0:
        count = n - col - 1
    elif direction == 1:
        count = col
    elif direction == 2:
        count = n - row - 1
    else:
        count = row

    nrow = row + dx[direction]
    ncol = col + dy[direction]

    for _ in range(count):

        if games[row][col] == games[nrow][ncol]:
            games[nrow][ncol] = 2 * games[row][col]
            games[row][col] = 0

            break

        elif games[nrow][ncol] == 0:
            games[nrow][ncol], games[row][col] = games[row][col], games[nrow][ncol]
    
        
        nrow += dx[direction]
        ncol += dy[direction]

        row += dx[direction]
        col += dy[direction]

def start(games,step,direction):
    global result 

    if step == 5:
        return
    
    next_games = copy.deepcopy(games)
    # right
    if direction == 0:
        for col in range(n-2,-1,-1):
            for row in range(n):
                move(next_games,row,col,direction)
    
    # left
    elif direction == 1:
       for col in range(1,n):
            for row in range(n):
                move(next_games,row,col,direction) 
    # down
    elif direction == 2:
        for row in range(n-1,-1,-1):
            for col in range(n):
                move(next_games,row,col,direction) 
    # up
    else:
        for row in range(1,n):
            for col in range(n):
                move(next_games,row,col,direction) 

    result = max(result,max(map(max, next_games)))

    # print(*next_games, sep='\n')
    # print()

    for d in range(4):
        start(next_games,step+1, d)
                
for i in range(4):
    start(games,0,i)

print(result)