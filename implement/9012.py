t = int(input())
for _ in range(t):
    stack = []
    problem = input()
    for p in problem:
        if p == '(':
            stack.append(p)
        else:
            if stack:
                stack.pop(-1)
            else:
                stack.append(False)
                break
    if stack:
        print("NO")
    else:
        print("YES")
