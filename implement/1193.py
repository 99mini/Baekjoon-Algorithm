import math

n = int(input())

x , y = 1 , 1

m = math.ceil((-1+math.sqrt(1+n*8))/2) 

sum = 0
for i in range(m):
  sum += i

order = n - sum

if m % 2 != 0:
  x = m - order + 1
  y = order
else:
  y = m - order + 1
  x = order

print(str(x)+'/'+str(y))
