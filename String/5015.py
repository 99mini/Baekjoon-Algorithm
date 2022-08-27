# https://www.acmicpc.net/problem/5015
# ls
# DP 

# TODO

# arg가 file의 substring 인지 확인
arg = input().split('*')
arg = "".join(arg)

def lcs(string1, string2):
    LCS_string = ''
    string1 = ' ' + string1
    string2 = ' ' + string2
    len_string1 =len(string1)
    len_string2 =len(string2)

    LCS = [[0 for _ in range(len_string1)] for _ in range(len_string2)]

    for i, str2 in enumerate(string2):
        for j, str1 in enumerate(string1):
            if i == 0 or j == 0:
                LCS[i][j] = 0 
            elif str1 == str2:
                LCS[i][j] = LCS[i-1][j-1] + 1
            else:
                LCS[i][j] = max(LCS[i-1][j],LCS[i][j-1])

    # find LCS 
    ni = i
    nj = j

    while LCS[ni][nj] != 0:
        recent = LCS[ni][nj]
        if recent == LCS[ni-1][nj]:
            ni -= 1
        elif recent == LCS[ni][nj-1]:
            nj -= 1
        else:
            LCS_string += string1[nj]
            ni -= 1
            nj -= 1 

    return LCS_string[::-1]

t = int(input())
for _ in range(t):
    file = input()
    if arg == lcs(arg,file):
        print('\n',file)