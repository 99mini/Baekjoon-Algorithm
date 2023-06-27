import sys
input = sys.stdin.readline

n = int(input())
crystals = list(map(int,input().split()))
max_value = -1

def search(crystals:list, value):
    global max_value
    if len(crystals) == 2:
        return value
    
    for i in range(len(crystals)-2):
        e = crystals[i] * crystals[i+2]
        removed_crystals = crystals.copy()
        removed_crystals.pop(i+1)
        return_value = search(removed_crystals,value+e)
        if return_value > max_value:
            max_value = return_value

    return value
search(crystals, 0)
print(max_value)