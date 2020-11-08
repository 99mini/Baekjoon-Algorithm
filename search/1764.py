n, m = map(int, input().split())

not_see = set()
not_listen = set()
not_see_listen = []

for i in range(n):
  not_see.add(str(input()))
for i in range(m):
  not_listen.add(str(input()))

if n > m:
  for l in not_listen:
    if l in not_see: 
      not_see_listen.append(l)
else:
  for s in not_see:
    if s in not_listen: 
      not_see_listen.append(s)

not_see_listen.sort()
print(len(not_see_listen))
for i in not_see_listen:
  print(i)
