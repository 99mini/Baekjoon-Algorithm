n = int(input())
datas = list(map(int, input().split()))

datas.sort()

if n % 2 == 0:
  print(datas[n//2 - 1])
else:
  print(datas[n//2])
