# LCS Longest Common Subsequence
# 가장 긴 부분 수열의 길이

string1 = input()
string2 = input()

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

print(LCS[i][j])