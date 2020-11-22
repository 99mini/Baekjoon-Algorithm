import heapq

n = int(input())
datas=[]
for _ in range(n):
  heapq.heappush(datas ,int(input()))
result = 0
while len(datas) != 1:
  one = heapq.heappop(datas)
  two = heapq.heappop(datas)
  new_value = one+two
  result += new_value
  heapq.heappush(datas, new_value)

print(result)
