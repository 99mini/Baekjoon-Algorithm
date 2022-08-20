# LCS 3
# 참고: LCS 9521.py

# TODO
# 1번과 2번의 LCS 를 구하고 3번과의 LCS 를 다시 구하는 경우 
# -> 처음 구한 LCS 가 여러개인 경우 답이 틀릴 수 있다...!

string1 = input()
string2 = input()
string3 = input()

string1 = ' ' + string1
string2 = ' ' + string2
len_string1 =len(string1)
len_string2 =len(string2)

LCS = [[0 for _ in range(len_string1)] for _ in range(len_string2)]
LCS_string = ''

# LCS 길이 테이블 완성
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

string1 = ' ' + LCS_string[::-1]
string2 = ' ' + string3
len_string1 =len(string1)
len_string2 =len(string2)

LCS = [[0 for _ in range(len_string1)] for _ in range(len_string2)]

# LCS 길이 테이블 완성
for i, str2 in enumerate(string2):
    for j, str1 in enumerate(string1):
        if i == 0 or j == 0:
            LCS[i][j] = 0 
        elif str1 == str2:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j],LCS[i][j-1])

print(LCS[i][j])