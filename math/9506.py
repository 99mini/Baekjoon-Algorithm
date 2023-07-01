import sys

input = sys.stdin.readline

while True:
    p = int(input())

    if p == -1:
        break

    divisors = []

    for i in range(1,p):
        if p % i == 0:
            divisors.append(i)

    if p == sum(divisors):
        print(p, " = ", " + ".join(map(str,divisors)), sep="")
    else:
        print(p , "is NOT perfect.")