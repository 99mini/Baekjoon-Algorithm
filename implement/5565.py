total = int(input())
datas = []
for _ in range(9):
  datas.append(int(input()))

prices = sum(datas)

print(total - prices)
