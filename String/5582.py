# 공통 부분 문자열

string1 = input()
string2 = input()
string1 = " " + string1
string2 = " " + string2
result = 0

dp = [[0 for _ in range(len(string1))] for _ in range(len(string2))]

for i, str2 in enumerate(string2):
    for j, str1 in enumerate(string1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif str1 == str2:
            dp[i][j] = dp[i-1][j-1] + 1
            if result < dp[i][j]:
                result = dp[i][j]
        else:
            dp[i][j] = 0
        
print(result)
