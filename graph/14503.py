import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())
# 좌표 (x,y) 방향 d
x, y, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]

# u r d l
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

result = 0

def run(x, y, d):
    global result
    visited[x][y] = True
    result += 1

    d -= 1
    if d < 0 :
        d += 4
    for i in range(4):
        # 회전
        next_d = d - i
        if next_d < 0: 
            next_d += 4

        next_x = x + move[next_d][0]
        next_y = y + move[next_d][1]
        if next_x > n or next_y > n or next_x < 0 or next_y < 0:
            return
        
        # 방문하지 않았고 벽이 아닌 경우
        if room[next_x][next_y] == 0 and not visited[next_x][next_y]:

            print(*visited,sep='\n', end='\n\n')

            run(next_x, next_y, next_d)

run(x, y, d)
print(result)