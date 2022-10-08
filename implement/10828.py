from sys import stdin

stack = []
t = int(stdin.readline())

for _ in range(t):
    operation = stdin.readline().split()
    if operation[0] == 'pop': 
        if stack:
            print(stack.pop(-1))
        else:
            print(-1)
    elif operation[0] == "size":
        print(len(stack))
    elif operation[0] =="empty":
        if stack:
            print(0)
        else:
            print(1)
    elif operation[0] =="top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
    else:
        stack.append(operation[1])
