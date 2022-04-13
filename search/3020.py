# https://www.acmicpc.net/problem/3020
# 이진 탐색
# 구간 합
# TODO
n,h=map(int,input().split())

broken_cnt = 200_001
case_cnt = 0
top_prefix = n//2
bottom_prefix = 0

t = {}
b = {}

for idx in range(n):
    value = int(input())
    # 석순
    if idx % 2 == 0:
        if value in t:
            t[value] += 1
        else:
            t[value] = 1
    # 종유석
    else:
        if h - value + 1 in b:
            b[h - value + 1] += 1
        else:
            b[h - value +1] = 1


for level in range(1,h+1):
    if level in b:
        bottom_prefix += b[level]

    if broken_cnt > top_prefix + bottom_prefix:
        case_cnt = 1
        broken_cnt = top_prefix + bottom_prefix
    elif broken_cnt == top_prefix + bottom_prefix:
        case_cnt += 1
    
    if level in t:
        top_prefix -= t[level]

print(broken_cnt, case_cnt)