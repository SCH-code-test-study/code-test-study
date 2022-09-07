n = int(input())
human_list = []

for _ in range(n):
    human = list(map(int, input().split()))
    human_list.append(human)

for i in range(n):
    rank = n
    for s in range(n):
        if i != s:
            if (human_list[i][0] > human_list[s][0]) and (human_list[i][1] > human_list[s][1]):
                rank -= 1
            elif (human_list[i][0] >= human_list[s][0]) or (human_list[i][1] >= human_list[s][1]):
                rank -= 1

    print(rank, end=" ")
