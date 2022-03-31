# https://www.acmicpc.net/problem/10158

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

# 일반적 구현
# 시간 초과
# a_w, a_h = 1, 1

# for _ in range(t):
#     p += a_w
#     q += a_h
#     # 좌우 벽에 부딪혔을 때
#     if p == w or p == 0:
#         a_w *= -1
#     # 상하 벽에 부딪혔을 때
#     if q == h or q == 0:
#         a_h *= -1

# ad-hoc 구현
# 정답 코드
p += t

interval_w = p % w
if (p // w) % 2 == 0:
    x = interval_w
else:
    x= w - interval_w

q += t

interval_h = q % h
if (q // h) % 2 == 0:
    y = interval_h
else:
    y = h - interval_h

print(x,y)