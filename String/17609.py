import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    string = sys.stdin.readline().strip()
    pseudo = False
    result = 0
    start = 0
    end = len(string) - 1
    while start < end:
        if string[start] == string[end]:
            start += 1
            end -= 1
        elif string[start + 1] == string[end] or string[start] == string[end-1]:
            tmp_start = start
            tmp_end = end

            start += 2
            end -= 1
            result = 1
            pseudo = True
            while start < end:
                if string[start] == string[end]:
                    start += 1
                    end -= 1
                else:
                    result = 2
                    pseudo = False
                    break
            
            start = tmp_start
            end = tmp_end
            if not pseudo:
                start += 1
                end -= 2
                result = 1
                pseudo = True
                while start < end:
                    if string[start] == string[end]:
                        start += 1
                        end -= 1
                    else:
                        result = 2
                        pseudo = False
                        break
            break
                
        else:
            result = 2
            break
    print(result)
                    