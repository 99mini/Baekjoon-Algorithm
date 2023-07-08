import sys

input = sys.stdin.readline

n = int(input())

result = 0
x,y = [], []
for _ in range(n):
    tx,ty = map(int, input().split())
    x.append(tx)
    y.append(ty)

print((max(x)-min(x))*(max(y)-min(y)))