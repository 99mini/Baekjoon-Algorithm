import sys

input = sys.stdin.readline

n,m = map(int,input().split())
words = {}

for _ in range(n):
    word = input().rstrip()

    if len(word) < m:
        continue

    if word in words:
        words[word] += 1
    else:
        words[word] = 1

word_list = []
for word in words:
    word_list.append([word,words[word]])

word_list.sort(key=lambda x : (-x[1],-len(x[0]), x[0]))

for word in word_list:
    print(word[0])