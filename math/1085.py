import math
x, y, w, h = map(int, input().split())
if w>x and h>y:
  print(min(w-x,h-y,x,y))
elif w>x and h<y:
  print(y-h)
elif w<x and h<y:
  print(x-w)
else:
  print(int(math.sqrt((x-w)*(x-w)+(y-h)*(y-h))))
