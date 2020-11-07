t = int(input())
result = []
for i in range(t):
  h, w, n = map(int, input().split())
  floor = n % h 
  if floor == 0:
    floor += h
    num = n // h
  else:
    num = n // h + 1

  if num < 10 : 
    result.append(str(floor)+"0"+str(num))
  else:
    result.append(str(floor)+str(num))

for i in result:
  print(i)
