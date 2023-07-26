import sys

input = sys.stdin.readline

vowel = ["a","e","i","o","u"]
while True:
    a = input().strip()
    if a == 'end':
        break
    isContinuity = False
    isRepeat = False
    isVowel = False

    for i in range(len(a)):
        if not isVowel:
            isVowel = a[i] in vowel
        if not isRepeat:
            if i + 1 < len(a):
                if a[i] == a[i+1]:
                    if not (a[i] == 'e' or a[i] == 'o'):
                        isRepeat = True
                        break
        if not isContinuity:
            if i + 2 < len(a):
                if len(set((a[i] in vowel, a[i+1] in vowel, a[i+2] in vowel))) == 1:
                    isContinuity = True
                    break

    if not isVowel or isContinuity or isRepeat:
        print(f'<{a}> is not acceptable.')
    else:
        print(f'<{a}> is acceptable.')