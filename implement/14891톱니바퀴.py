#https://www.acmicpc.net/problem/14891
#
#if direction is 1, clockwise else if direction is -1, counterclockwise   
def rotation(gear: str, number:int, direction: int):
  #rotation clockwise
  if direction == 1:
    gears[number] = gear[-1] + gear[:-1]
  #rotation counterclockwise
  elif direction == -1:
    gears[number] = gear[1:] + gear[1]
  return gears

def compare(rotated_gear: str, compare_gear: str, pos: str, direction: int):
  # 오른쪽과 비교하는 경우
  if pos == 'R':
    # 극이 다른 경우 direction과 반대 방향으로 회전
    if rotated_gear[2] != compare_gear[6]:
      return True, -1*direction

  # 왼쪽과 비교하는 경우    
  elif pos == 'L':
    if rotated_gear[6] != compare_gear[2]:
      return True, -1*direction

  return False, direction

# main
gears = []
for _ in range(4): 
  gears.append(input())

k = int(input())

for _ in range(k):
  number, direction = map(int,  input().split())

  switch, directions = [False, False, False, False], [1,1,1,1]
  switch[number-1], directions[number-1] = True, direction
  
  # 연쇄 회전 처리
  if number == 1:
    switch[1], directions[1] = compare(gears[number-1], gears[1], 'R', direction)
    if switch[1]:
      switch[2], directions[2] = compare(gears[1], gears[2],'R', directions[1])
    if switch[2]:
      switch[3], directions[3] = compare(gears[2], gears[3],'R', directions[2])

  elif number == 2:
    switch[0], directions[0] = compare(gears[number-1], gears[0],'L', direction)
    switch[2], directions[2] = compare(gears[number-1], gears[2],'R', direction)
    if switch[2]:
      switch[3], directions[3] = compare(gears[2],gears[3],'R', directions[2])

  elif number == 3:
    switch[1], directions[1] = compare(gears[number-1], gears[1],'L', direction)
    if switch[1]:
      switch[0], directions[0] = compare(gears[1], gears[0],'L', directions[1])
    switch[3], directions[3] = compare(gears[number-1], gears[3],'R', direction)

  else:
    switch[2], directions[2] = compare(gears[number-1], gears[2],'L', direction)
    if switch[2]:
      switch[1], directions[1] = compare(gears[2], gears[1],'L', directions[2])
    if switch[1]:
      switch[0], directions[0] = compare(gears[1], gears[0],'L', directions[1])

  print(switch, directions)
  print(gears)
  for i in range(4):
    if switch[i]:
      rotation(gears[i], i, directions[i])
  print(gears)
  
score = 0
for i in range(4):
  # S극인 경우 
  if gears[i][0] == '1':
    score += 2**i

print(score)
