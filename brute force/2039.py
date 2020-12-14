from itertools import combinations

data = []
for _ in range(9):
  data.append(int(input()))

seven_data = combinations(data, 7)
for seven in seven_data:
  length = sum(seven)
  if length == 100:
    seven = list(seven)
    seven.sort()
    break

for s in seven:
  print(s)
