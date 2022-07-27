'''
10 2
3 -2 -4 -9 0 3 7 13 8 -3

21

10 5
3 -2 -4 -9 0 3 7 13 8 -3

31
'''

N, K = map(int, input().split())
numbers = list(map(int,input().split()))
result =[sum(numbers[:K])]
for idx in range(1, N-K+1):
    result.append(result[-1] - numbers[idx - 1] + numbers[idx + K -1])

print(max(result))

