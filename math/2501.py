import sys

input = sys.stdin.readline

p,q = map(int,input().split())

divisors = []

for i in range(1,p+1):
    if p % i == 0:
        divisors.append(i)

if q > len(divisors):
    print(0)
else:
    print(divisors[q-1])