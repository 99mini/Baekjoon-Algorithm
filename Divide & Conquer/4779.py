import sys
def f(start, n):
    if n == 1:
        return
    for i in range(start + n//3, start + 2*(n//3)):
        result[i] = ' ' 
    f(start,n//3)
    f(start + 2* (n // 3), n//3)

while True:
    try :
        N = int(sys.stdin.readline())
        result = ['-']*(3**N)
        f(0,3**N) 
        print(''.join(result))
    except : 
        break 