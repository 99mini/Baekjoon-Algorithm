import sys

input = sys.stdin.readline

n,w,L = map(int,input().split())

trucks = list(map(int,input().split()))

bridge = [0 for _ in range(w)]
times = 0
count = 0

while count < n:
    # 한 칸 전진
    bridge = bridge[1:] + [0]
    times += 1

    if L >= sum(bridge) + trucks[count]: 
        bridge[-1] = trucks[count]
        count += 1

print(times + w)