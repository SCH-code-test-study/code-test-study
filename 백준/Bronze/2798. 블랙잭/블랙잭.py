n, m = map(int, input().split())
cards = list(map(int, input().split()))

val = 0
for i in range(n - 2):
    for ii in range(i+1, n-1):
        for iii in range(ii+1, n):
            com = cards[i] + cards[ii] + cards[iii]
            if (val < com) and com <= m:
                val = com

print(val)
