a,b,v = map(int,input().split())
m = (v - b) // (a - b)
n = (v - b) % (a - b)

if n != 0:
    m += 1

print(m)