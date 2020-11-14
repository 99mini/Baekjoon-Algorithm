n = int(input())
datas = list(map(int, input().split()))
vote = [0] * 101
members = []

for i in datas:
  vote[i] += 1

imposter = 0
for i in range(1, n+1):
  members.append([vote[i], i])

members.sort(reverse=True)

if members[0][0] > members[1][0]:
  print(members[0][1])
else:
  print('skipped')
