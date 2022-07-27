n = int(input())
m = int(input())

result_sum = 0
result_min = -1

for number in range(n,m+1):
    if number == 1:
        continue
    isPrime = True
    for i in range(2, int(number ** 0.5+1)):
        if number % i == 0:
            isPrime = False
            break
    if isPrime:
        result_sum += number
        if result_min < 0:
            result_min = number
    
if result_sum == 0:
    print(-1)
else:
    print(result_sum, result_min, sep='\n')
