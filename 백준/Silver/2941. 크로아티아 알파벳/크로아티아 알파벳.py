st = input()
leng = len(st)
count = 0
i = 0

while i < leng:
    if st[i] == "c" or st[i] == "s" or st[i] == "z":
        if i+1 < leng:
            if (st[i+1] == "=") or (st[i] == "c" and st[i+1] == "-"):
                count = count + 1
                i = i+2
            else:
                count += 1
                i += 1
        else:
            count += 1
            i += 1
        continue
    elif st[i] == "l" or st[i] == "n":
        if i+1 < leng:
            if st[i + 1] == "j":
                count = count + 1
                i = i+2
            else:
                count += 1
                i += 1
        else:
            count += 1
            i += 1
        continue
    elif st[i] == "d":
        if i+1 < leng:
            if (st[i+1] == "-"):
                count = count + 1
                i = i+2
            elif i+2 < leng:
                if (st[i+1] == "z" and st[i+2] == "="):
                    count = count + 1
                    i += 3
                else:
                    count = count + 1
                    i += 1
            else:
                count = count + 1
                i += 1
        else:
            count = count + 1
            i += 1
        continue
    else:
        count += 1
        i = i+1


print(count)
