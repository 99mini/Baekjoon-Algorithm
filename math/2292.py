import math

x = int(input())

n = (3 + math.sqrt(9 + 12 * (x - 1))) / 6

print(math.ceil(n))
