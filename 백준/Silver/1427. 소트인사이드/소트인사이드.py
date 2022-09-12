n = input()
li = []

for a in n:
    li.append(a)

li.sort(reverse=True)

print(''.join(li))
