import sys

input = sys.stdin.readline

s = input().strip()
q = int(input())

arr = [[0 for _ in range(26)] for _ in range(len(s))]

arr[0][ord(s[0]) - ord('a')] = 1
for i in range(1, len(s)):
    arr[i][ord(s[i]) - ord('a')] = 1
    for j in range(26):
        arr[i][j] += arr[i - 1][j]

for _ in range(q):
    a,start,end = map(str, input().split())

    start = int(start)
    end = int(end)

    if start == 0:
        res = arr[end][ord(a) - ord('a')]
    else:
        res = arr[end][ord(a) - ord('a')] - arr[start - 1][ord(a) - ord('a')]
    print(res)