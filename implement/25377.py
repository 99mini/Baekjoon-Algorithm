n = int(input())
result = 1001
for _ in range(n):
    a, b = map(int,input().split())
    if a <= b:
        result = min(b, result)

if result == 1001:
    print(-1)
else:
    print(result)