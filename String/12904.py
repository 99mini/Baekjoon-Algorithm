string1 = input()
string2 = input()

while string2 != string1:
    if len(string2) == 0:
        print("0")
        exit()
    if string2[-1] == 'A':
        string2 = string2[:-1]
    elif string2[-1] == 'B':
        string2 = string2[::-1]
        string2 = string2[1:]
    else:
        print("0")
        exit()
print("1")