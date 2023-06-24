import sys

input = sys.stdin.readline

n,k = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]
pieces = []
cnt = 0

for _ in range(k):
    r,c,d = map(int,input().split())
    r -= 1
    c -= 1
    d -= 1

    pieces.append([r,c,d])


q = [[[i+1, pieces[i]]] for i in range(n)] 

dx = [0,0,-1,1]
dy = [1,-1,0,0]


def checkBound(row,col):
    if row < n and row >= 0 and col < n and col >= 0:
        return True
    else:
        return False

while True:
    cnt += 1
    if cnt > 1000:
        print(-1)
        break
    for _ in q:
        if len(_) == k:
            print(cnt)
            break
    print(cnt)
    print(*q, sep='\n')
    for idx,piece in enumerate(q):
        if not piece:
            continue
        origin_pieces = piece
        piece = piece[-1]

        number = piece[0]
        row, col, direction = piece[1]

        nrow = row + dx[direction]
        ncol = col + dy[direction]

        # 범위를 벗어나는 경우
        if checkBound(nrow, ncol):
            # 0 or 2 이면 +1
            if direction % 2 == 0:
                direction += 1
            else:
                direction -= 1

            nrow = row + dx[direction]
            ncol = col + dy[direction]

            if checkBound(nrow, ncol):
                origin_pieces[-1][1][-1] = direction
                for stack in origin_pieces:
                    stack[1][0], stack[1][1] = nrow, ncol

        elif checkBound(nrow, ncol):
            color = board[nrow][ncol]
            # 흰색 0 : 이동
            if color == 0:
                for stack in origin_pieces:
                    stack[1][0], stack[1][1] =nrow,ncol
            # 빨간색 1 : 이동 후 리스트 뒤집기
            elif color == 1:
                for stack in origin_pieces:
                    stack[1][0], stack[1][1] =nrow,ncol
                q[idx].reverse()
            # 파란색 2 : 이동방향 바꾸고 이동
            elif color == 2:
                # 0 or 2 이면 +1
                if direction % 2 == 0:
                    direction += 1
                else:
                    direction -= 1

                nrow = row + dx[direction]
                ncol = col + dy[direction]
                origin_pieces[-1][1][-1] = direction

                if checkBound(nrow, ncol):
                    for stack in origin_pieces:
                        stack[1][0], stack[1][1] =nrow, ncol
                

        


        # 움직임이 끝나면 겹치는 것이 있는 지 확인
        for cmp_idx,cmp_q in enumerate(q):
            if not cmp_q:
                continue
            cmp_q_top = cmp_q[0]
            cmp_number = cmp_q_top[0]
            cmp_row, cmp_col = cmp_q_top[1][0], cmp_q_top[1][1]

            if cmp_number != number:
                # 위치가 겹친다면    
                if nrow == cmp_row and ncol == cmp_col:
                    for new_q in cmp_q:
                        q[idx].append(new_q) 
                    q[cmp_idx] = []
                    break



         


