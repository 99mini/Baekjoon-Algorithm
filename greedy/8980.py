import sys
input = sys.stdin.readline

n,c = map(int,input().split())
m = int(input())

arr = [list(map(int,input().split())) for _ in range(m)]

trucks = [0 for _ in range(n+1)]

result = 0

arr.sort(key=lambda x: (x[1],x[0]))

for a in arr:
    start, end, weight = a
    max_item = max(trucks[start:end])
    delivary_item = min(c-max_item, weight)

    if delivary_item > 0:
        for i in range(end-start):
            trucks[start+i] += delivary_item

    result += delivary_item

print(result)
