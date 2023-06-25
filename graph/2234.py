import sys
from collections import deque

input = sys.stdin.readline

def dec2bin(dec):
    bin = []
    while dec:
        if dec % 2 == 1:
            bin.append(1)
        else:
            bin.append(0)
        dec //= 2
    while len(bin) < 4:
        bin.append(0)
    bin = bin[::-1]
    return bin

def bfs(row,col):
    cnt = 1
    dq.append([row,col])
    visited[row][col] = rooms

    while dq:
        curr_row, curr_col = dq.popleft()
        walls = castle[curr_row][curr_col]
        walls_bin = dec2bin(walls)

        for i in range(4):
            if walls_bin[i]:
                continue
            nrow, ncol = curr_row + dx[i], curr_col + dy[i]

            if nrow < m and nrow >= 0 and ncol < n and ncol >=0:
                if visited[nrow][ncol] == 0:
                    dq.append([nrow,ncol])
                    cnt += 1
                    visited[nrow][ncol] = rooms
    return cnt

n,m = map(int,input().split())

castle = [list(map(int,input().split())) for _ in range(m)]

visited = [[0 for _ in range(n)]for _ in range(m)]

rooms = 0
room_sizes = []
max_two_room_size = -1

dq = deque()

# d r u l
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(m):
    for j in range(n):
        if visited[i][j] == 0:
            rooms += 1
            room_sizes.append(bfs(i,j))

for i in range(m):
    for j in range(n):
        for k in range(4):
            nrow, ncol = i + dx[k], j + dy[k]
            
            if nrow < m and nrow >= 0 and ncol < n and ncol >=0:
                current_room_number = visited[i][j] - 1
                next_room_number = visited[nrow][ncol] - 1
                if current_room_number != next_room_number:
                    max_two_room_size = max(max_two_room_size,room_sizes[current_room_number] + room_sizes[next_room_number])

print(rooms)
print(max(room_sizes))
print(max_two_room_size)
