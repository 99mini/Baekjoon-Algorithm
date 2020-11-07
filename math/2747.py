n = int(input())
data = [-1 for _ in range(46)]

def fibo(n):
  if n < 2:
    data[n] == n
    return n
  elif n == 2:
    data[2] == 1
    return 1
  else:
    if data[n] == -1:
      data[n] = fibo(n-1) + fibo(n-2)
      return data[n]
    else:
      return data[n] 

print(fibo(n))
