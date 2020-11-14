n, h, w = map(int, input().split())
datas = []
result = ['?'] * n

for i in range(h):
  datas.append(str(input()))

for data in datas:
  for idx ,apla in enumerate(data):
    if apla != '?':
      result[idx // w] = apla

print(''.join(result)) 
