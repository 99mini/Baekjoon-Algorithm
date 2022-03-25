# https://www.acmicpc.net/problem/24725

from functools import reduce


n, m = map(int,input().split())
matrix = [str(input()) for _ in range(n)]

result = 0

def is_mbti(str):
    if len(str) != 4:
        return False

    mbti = [['E','I'],['S','N'],['F','T'],['J','P']]
    mbti_bool1 = [False, False, False, False]
    mbti_bool2 = [False, False, False, False]


    for idx in range(4):
        if str[idx] in mbti[idx]:
            mbti_bool1[idx] = True
        if str[idx] in mbti[3-idx]:
            mbti_bool2[3-idx] = True

    return reduce(lambda result, curr: result and curr, mbti_bool1, True) or reduce(lambda result, curr: result and curr, mbti_bool2, True)

for row in range(n):
    for col in range(m):
        # 가로
        testcase = ''
        for c in range(col,col+4):
            if col+4 > m:
                break
            testcase += matrix[row][c]
        if is_mbti(testcase):
            # print(testcase)
            result += 1

        # 세로
        testcase = ''
        for r in range(row,row+4):
            if row+4 > n:
                break
            testcase += matrix[r][col]
        if is_mbti(testcase):
            # print(testcase)
            result += 1

        # 대각선 좌 -> 우
        testcase = ''
        for i in range(4):
            if row+4 > n or col+4 > m:
                break
            testcase += matrix[row+i][col+i]
        if is_mbti(testcase):
            # print(testcase)
            result += 1
            
        # 대각선 우 -> 좌
        testcase = ''
        for i in range(4):
            if row+4 > n or col-3 < 0:
                break
            testcase += matrix[row+i][col-i]
        if is_mbti(testcase):
            # print(testcase)
            result += 1
        

print(result)