m = int(input())
f = [list(map(int,input().split()))]
q = int(input())

end_point = [0 for _ in range(m)]

for i in range(q):
    n,x = map(int,input().split())
    nx = x
    prev_len = len(f)
    while len(f) < n:
        f.append([0 for _ in range(m)])

    if f[n-1][x-1] != 0:
        print(f[n-1][x-1])
        continue

    for j in range(end_point[x-1],n-1):
        f[j+1][x-1] = f[0][f[j][x-1]-1]
    
    end_point[x-1] = n - 1
    print(f[n-1][x-1])