import sys
input = sys.stdin.readline

n = int(input())
li = []
dic = {}

for _ in range(n):
    a, b = map(int, input().split())
    if b in dic:
        dic[b].append(a)
    else:
        dic[b] = [a]


sorted_dict = sorted(dic.items())
result_dic = {}

for i in range(len(sorted_dict)):
    result_dic[sorted_dict[i][0]] = sorted(sorted_dict[i][1])

for y, lix in result_dic.items():
    for x in lix:
        print(x, end=" ")
        print(y)
