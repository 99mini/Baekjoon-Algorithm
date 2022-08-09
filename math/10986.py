'''
입력
첫째 줄에 N과 M이 주어진다. (1 ≤ N ≤ 106, 2 ≤ M ≤ 103)

둘째 줄에 N개의 수 A1, A2, ..., AN이 주어진다. (0 ≤ Ai ≤ 109)

출력
첫째 줄에 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 출력한다.

5 3
1 2 3 1 2

7
'''


import sys


N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
prefix_sum_list = A.copy()
result = 0

for interval in range(1, N+1):
    print("interval: ", interval,"\t", prefix_sum_list)
    result += len([x for x in prefix_sum_list if x % M == 0])

    for i in range(N-interval):
        prefix_sum_list[i] += A[i+interval]
    prefix_sum_list = prefix_sum_list[:N-interval]

print(result)