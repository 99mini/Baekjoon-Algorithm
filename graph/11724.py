def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

n, k = map(int, input().split())
datas = []

parent = [0] * (n + 1)
for i in range(1, n+1):
  parent[i] = i

for _ in range(k):
  u, v = map(int, input().split())
  union_parent(parent, u, v)

for i in range(1, n+1):
  parent[i] = find_parent(parent, i)

parent = set(parent)

print(len(parent) - 1)
