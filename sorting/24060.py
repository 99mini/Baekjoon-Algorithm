import sys

input = sys.stdin.readline

def merge_sort(arr):

    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)
        

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                saved.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                saved.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            saved.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            saved.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]
            
    return sort(0, len(arr))

n,k = map(int,input().split())
A = list(map(int,input().split())) 
saved = []
merge_sort(A)

if len(saved) >= k:
    print(saved[k-1])
else:
    print(-1)