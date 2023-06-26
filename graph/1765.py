import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
    

state = [list(map(int,input().split())) for _ in range(m)]

'''
1. 그래프를 순회하며 인접한 노드의 엣지를 비교
2. 엣지를 비교했을 때 한 쌍의 엣지의 값이 같은 경우
    -> 탐색한 두 노드를 F 로 연결 
    => F 로 연결되어 있으면 하나로 묶음 (리스트의 가장 앞의 노드 번호로 바꿈)
3. 새롭게 연결된 엣지가 없을 때 까지 1., 2. 반복
'''


