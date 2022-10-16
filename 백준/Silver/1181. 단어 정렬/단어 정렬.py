import sys

n = int(sys.stdin.readline())
li = []

for _ in range(n):
    li.append(sys.stdin.readline().strip())
# 값 넣기

li = list(set(li))
li.sort()
# 중복 값 제거한 뒤 알파벳 순으로 정렬
li.sort(key=len)

# for l in range(1, 51):
#     for st in li:
#         if len(st) == l:
#             a.append(st)

for s in li:
    print(s)
