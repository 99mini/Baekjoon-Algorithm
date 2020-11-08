n = int(input())
ns = list(map(int, input().split()))

m = int(input())
ms = list(map(int, input().split()))

def binary_search(arr, target, start, end):
  while start <= end:
    mid = (start+end) // 2

    if arr[mid] == target:
      return mid
    elif arr[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None

ns.sort()

for m in ms:
  result = binary_search(ns,m,0,n-1)
  if result == None:
    print(0)
  else:
    print(1)
