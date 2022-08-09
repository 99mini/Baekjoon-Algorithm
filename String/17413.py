string = input()
result = ''
tag = False
sub_string = ''

for s in string:
    if s == '<':
        result += sub_string[::-1]
        sub_string = ''
        result += s
        tag = True
    elif s == '>':
        result += sub_string
        sub_string = ''
        result += s
        tag = False
    else:
        if tag:
            result += s
        else:
            if s == " ":
                result += sub_string[::-1]
                sub_string = ''
                result += s
            else:
                sub_string += s
if sub_string:
    result += sub_string[::-1]
    
print(result)