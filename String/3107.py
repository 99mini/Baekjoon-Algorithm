# TODO
addr = input()
addr = addr.split(":")
if addr.count('') == 2:
    addr.remove('')
result = []
print(addr)
for a in addr:
    if not a:
        for _ in range(9-len(addr)):
            result.append("0000")
    else:
        result.append("0" * (4 - len(a)) + a)

print(":".join(result))