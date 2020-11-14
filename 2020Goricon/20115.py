n = int(input())

datas = list(map(float, input().split()))

datas.sort()

for i in range(n-1):
  datas[len(datas) - 1] += datas[i] / 2

print('%.5f' %datas[len(datas) - 1]) 
