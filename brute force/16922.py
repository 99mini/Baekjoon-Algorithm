from itertools import combinations_with_replacement

numbers = [1,5,10,50]

n = int(input())
h = set(sum(i) for i in combinations_with_replacement(numbers, n))
print(len(h))
