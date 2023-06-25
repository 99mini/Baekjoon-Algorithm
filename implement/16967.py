import sys

input = sys.stdin.readline

h,w,x,y = map(int,input().split())

dupArr = [list(map(int,input().split())) for _ in range(h+x)]

originArr = [[0 for _ in range(w)] for _ in range(h)] 

def checkA(i,j):
    if i < h and j < w:
        return True
    else:
        return False
    
def checkB(i,j):
    if y <= j and x <= i :
        return True
    else:
        return False

for i in range(h):
    for j in range(w):
        if checkA(i,j):
            if checkB(i,j):
                originArr[i][j] = dupArr[i][j] - originArr[i-x][j-y]
            else:
                originArr[i][j] = dupArr[i][j]
            print(originArr[i][j], end=' ')
    print()