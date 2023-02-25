t = int(input())
building = list(map(int,input().split()))
result = -1
top_building = 0
for i in range(t):
    front = i - 1
    end = i + 1
    count = 0
    
    if front >= 0: 
        top_building = building[front]
        front -= 1
        count += 1
        while front >=0 and top_building < building[front]:
            top_building = max(building[front], top_building)
            count += 1
            front -= 1 

    if end < t: 
        top_building = building[end]
        end += 1
        count += 1
        while end < t and top_building < building[end]:
            top_building = max(building[front], top_building)
            count += 1
            end += 1 
    print("index:", i, "count:", count)
    result = max(result,count)

print(result)
