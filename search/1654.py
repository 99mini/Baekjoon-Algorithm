n, k = map(int, input().split())
data = []

for i in range(n):
  data.append(int(input()))

number = 0
result = 0
start = 1
end = max(data)
mid = (start + end) // 2

while start < end:
  number = 0
  mid = (start + end) // 2
  
  for i in data:
    number += i // mid
  
  if k > number:
    end = mid - 1
  else:
    result = mid
    start = mid + 1

if number >= k:
  result = mid

number = 0
for i in data:
    number += i // end
if number >= k:
  result = end
  
print(result)
