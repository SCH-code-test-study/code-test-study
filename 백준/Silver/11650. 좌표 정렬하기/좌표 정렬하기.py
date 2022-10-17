import sys
input = sys.stdin.readline

n = int(input())
li = []
dic = {}

for _ in range(n):
    a, b = map(int, input().split())
    if a in dic:
        dic[a].append(b)
    else:
        dic[a] = [b]


sorted_dict = sorted(dic.items())
result_dic = {}

for i in range(len(sorted_dict)):
    result_dic[sorted_dict[i][0]] = sorted(sorted_dict[i][1])

for key, li in result_dic.items():
    for val in li:
        print(key, end=" ")
        print(val)
