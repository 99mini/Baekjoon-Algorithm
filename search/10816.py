# https://www.acmicpc.net/problem/10816

import sys
input = sys.stdin.readline

n = int(input())
cards_n = list(map(int, input().split()))

m = int(input())
cards_m = list(map(int, input().split()))

card_dict = {}
for c in cards_n:
    if c in card_dict:
        card_dict[c] += 1
    else:
        card_dict[c] = 1

for c in cards_m:
    if c in card_dict:
        print(card_dict[c], end=' ')
    else:
        print(0, end=' ')