import sys
input = sys.stdin.readline

def mergeSort(a):
    if len(a) == 1:
        return a
    
    mid = (len(a) + 1)//2
    left = mergeSort(a[:mid])
    right = mergeSort(a[mid:])
    
    a2 = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a2.append(left[i])
            ans.append(left[i])
            i += 1
        else:
            a2.append(right[j])
            ans.append(right[j])
            j += 1
    
    while i < len(left):
        a2.append(left[i])
        ans.append(left[i])
        i += 1
        
    while j < len(right):
        a2.append(right[j])
        ans.append(right[j])
        j += 1
        
    return a2

n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = []
mergeSort(a)

if len(ans) >= k:
    print(ans[k-1])
else:
    print(-1) 
