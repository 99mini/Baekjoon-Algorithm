import sys

input = sys.stdin.readline

R, C, N = map(int,input().split())

tiles = []
boom_tiles1 = []
boom_tiles2 = []
all_boom_tiles = []

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for _ in range(R):
    tiles.append(list(input().strip()))
    boom_tiles1.append(['O' for _ in range(C)])
    boom_tiles2.append(['O' for _ in range(C)])
    all_boom_tiles.append(['O' for _ in range(C)])

def boom(row,col, boom_tiles):

    boom_tiles[row][col] = '.'
    for j in range(4):
        brow = dx[j] + row
        bcol = dy[j] + col
        if brow >=0 and brow < R and bcol >= 0 and bcol < C:
            boom_tiles[brow][bcol] = '.'

for i in range(R):
    for j in range(C):
        if tiles[i][j] == 'O': 
            boom(i,j, boom_tiles1)

for i in range(R):
    for j in range(C):
        if boom_tiles1[i][j] == 'O' : 
            boom(i,j, boom_tiles2)

if N == 1:
    result = tiles
elif N % 2 == 0:
    result = all_boom_tiles
elif N % 4 == 3:
    result = boom_tiles1
else:
    result = boom_tiles2

for t in result:
    print(''.join(t))