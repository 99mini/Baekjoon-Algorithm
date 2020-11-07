t = int(input())

data = [[0]*15 for _ in range(15)]

def a(k: int, n: int):
  if data[k][n] != 0:
    return data[k][n]
  else:
    if n == 1:
      data[k][1] = 1
      return 1
    elif k == 0:
      data[0][n] = n 
      return n
    else: 
      data[k][n] = a(k-1,n) + a(k, n-1)
      return data[k][n]
    
for i in range(t):
  k = int(input())
  n = int(input())

  print(a(k,n))
