#https://www.acmicpc.net/problem/1946
t = int(input())

for _ in range(t):
  n = int(input())
  employees = sorted([tuple(map(int, input().split())) for i in range(n)])
  cnt = 1
  Min = employees[0][1]

  for i in range(1,n):
    if Min > employees[i][1]:
      cnt += 1
      Min = employees[i][1]

  print(cnt)
