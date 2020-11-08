m, n = map(int, input().split())

prime = [0] * (n+1)
prime[1] = -1

for i in range(1, n + 1):
  if prime[i] == 0:
    for j in range(i*2, n+1, +i):
      prime[j] = -1

for i in range(m, n+1):
  if prime[i] == 0:
    print(i)
