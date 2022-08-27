string = input()

string = string.upper()
count=0
alpabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for alpa in alpabet:
    tmp = string.count(alpa)
    if count < tmp:
        count = tmp
        result = alpa
    elif count == tmp:
        result = '?'

print(result)