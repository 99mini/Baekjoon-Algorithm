import sys

n,k = map(int,sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().strip()))
result = []

for i in range(n):
    while k > 0 and result:
        if result[len(result)-1] < numbers[i]:
            result.pop()
            k -= 1
        else:
            break
    result.append(numbers[i])
    
while k > 0:
    result.pop()
    k -= 1

for i in range(len(result)):
    print(result[i], end="")