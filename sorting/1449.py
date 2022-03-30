# https://www.acmicpc.net/problem/1449

n, l = map(int,input().split())
pipe_pos = list(map(int, input().split()))

pipe_pos.sort()

result = 0
interval = 0
for i in range(n-1):
    interval += pipe_pos[i+1]-pipe_pos[i]
    if interval + 1 > l:
        result += 1
        interval = 0

print(result+1)
    