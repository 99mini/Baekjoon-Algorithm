# (100+1+ | 01)+
# TODO
t = int(input())

for _ in range(t):
    sign = input()
    is_sign = True
    while sign:
        if sign[:3] == '100':
            i = 0
            while 3 + i < len(sign) and sign[3 + i] == '0':
                i += 1
            while 3 + i < len(sign) and sign[3 + i] == '1':
                i += 1
            if 5 + i < len(sign) and sign[3 + i: 5 + i] == '00':
                sign = sign[2+i:]
            elif 3 + i < len(sign):
                sign = sign[3 + i:]
            else:
                if sign[-1] != '1':
                    is_sign = False
                break
        elif sign[:2] == '01':
            if len(sign) == 2:
                break
            else:
                sign = sign[2:]
        else:
            is_sign = False
            break
    if is_sign:
        print("YES")
    else:
        print("NO")