import sys

input = sys.stdin.readline

n = int(input())
cows = [list(map(int,input().split())) for _ in range(n)]

cows.sort(key=lambda x: x[0])

index = 0
current_cow = cows[index]
time = current_cow[0]

while index < n:
    if current_cow[0] <= time:
        time += current_cow[1]
        index += 1
        if index < n:
            current_cow = cows[index]
    else:
        time += 1

print(time)