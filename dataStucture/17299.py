import sys

input = sys.stdin.readline

n = int(input())

numbers = list(map(int,input().split()))

result = [-1] * n

cnt = dict()

stack = []

for i in numbers:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in range(n):
    while stack and cnt[numbers[stack[-1]]] < cnt[numbers[i]]:
        result[stack.pop()] = numbers[i]
    stack.append(i)

print(*result, sep=' ')