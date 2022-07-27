family = {}

n = int(input())
a,b = map(int,input().split())
m = int(input())
for _ in range(m):
    x,y = map(int,input().split())
    if x in family:
        family[x].append(y)
    else:
        family[x] = [y]

print(family)