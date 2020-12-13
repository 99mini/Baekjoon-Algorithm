#11404번 플로이드
n = int(input())
m = int(input())
INF = 123456789
matrix = [[INF]* (n+1) for _ in range(n+1)]

# m 개의 간선을 입력 받는다.
# 인접 행렬 형식 
for _ in range(m):
  a, b, c = map(int, input().split())

  # 만약 시작 도시와 도착 도시를 연결하는 노선이 여려개일 경우 최소값을 선택한다.
  matrix[a][b] = min(matrix[a][b], c)

# 플로이드-와샬 알고리즘 적용
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      matrix[a][b] = min(matrix[a][b], matrix[a][k] + matrix[k][b])

for row in range(1,n+1):
  for col in range(1,n+1):
    if row == col:
      print(0, end=' ')
    elif matrix[row][col] == INF:
      print(0, end=' ')
    else:
      print(matrix[row][col], end=' ')
  print()
