from collections import deque

C,R,H = map(int,input().split())

def isClear():
    for h in range(H):
        if any(False in element for element in tomatos[h]):
            return False
    return True

tomatos = [[list(map(int,input().split())) for _ in range(R)] for _ in range(H)]

dr = [0,0,0,0,1,-1]
dc = [1,-1,0,0,0,0]
dh = [0,0,1,-1,0,0]

cnt = 0

dq = deque()

visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(H)]

init_state = []

for h in range(H):
    for r in range(R):
        for c in range(C):
            if tomatos[h][r][c] == 1 and not visited[h][r][c]:
                init_state.append((h,r,c))
                visited[h][r][c] = True

dq.append(init_state)

while dq[0] and not isClear():

    state = dq.popleft()

    next_state = []
    for s in state:
        h,r,c = s

        for i in range(6):
            nr,nc,nh = r + dr[i], c + dc[i], h + dh[i]

            if nr >= 0 and nr < R and nc >= 0 and nc < C and nh >=0 and nh < H and not visited[nh][nr][nc] and tomatos[nh][nr][nc] == 0:
                tomatos[nh][nr][nc] = 1
                visited[nh][nr][nc] = True
                next_state.append((nh,nr,nc))

    dq.append(next_state)
    cnt += 1
        

if isClear():
    print(cnt)
else:
    print(-1)
    