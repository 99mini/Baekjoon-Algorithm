n = int(input())
times = list(map(int, input().split()))

def gcd(r1,r2):
    while r2:
       r1, r2 = r2, r1 % r2
  
    return r1

def lcm(a,b):
    return int(a*b / gcd(a,b))

while len(times) > 1:
    times.append(lcm(times[0],times[1]))
    times.pop(0)
    times.pop(0)

print(times[0])
