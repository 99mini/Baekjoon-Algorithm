t = int(input())
for _ in range(t):
  x1, y1 ,r1, x2, y2, r2 = map(int, input().split())

  if x1 == x2 and y1 == y2:
    if r1 == r2:
      print(-1)
    else:
      print(0)
    continue

  R1 = (r1 + r2)*(r1 + r2)
  R2 = (r1 - r2)*(r1 - r2)
  D = (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)

  if R1 < D or R2 > D:
    print(0)
  elif R1 == D or R2 == D:
    print(1)
  elif R1 > D or R2 < D:
    print(2)
