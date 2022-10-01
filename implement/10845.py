from sys import stdin

que = []
t = int(stdin.readline())

for _ in range(t):
    operation = stdin.readline().split()
    if operation[0] == 'pop': 
        if que:
            print(que.pop(0))
        else:
            print(-1)
    elif operation[0] == "size":
        print(len(que))
    elif operation[0] =="empty":
        if que:
            print(0)
        else:
            print(1)
    elif operation[0] =="front":
        if que:
            print(que[0])
        else:
            print(-1)
    elif operation[0] == "back":
        if que:
            print(que[-1])
        else:
            print(-1)
    else:
        que.append(operation[1])
