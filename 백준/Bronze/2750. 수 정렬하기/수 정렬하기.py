n = int(input())
li = []

for _ in range(n):
    a = int(input())
    li.append(a)

li.sort()

for a in li:
    print(a)
