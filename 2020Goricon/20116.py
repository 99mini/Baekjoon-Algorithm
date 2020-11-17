n, l = map(int, input().split())
xs = list(map(int, input().split()))
result = True
weight = sum(xs)

for i in range(n - 1):
  weight -= xs[i]
  center = weight / (n - i - 1)
  if xs[i] - l < center and xs[i] + l > center:
    continue
  else:
    result = False
    break

if result:
    print("stable")
else:
    print("unstable")
