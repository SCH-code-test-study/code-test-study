m, n = map(int, input().split())

scores = sorted(list(map(int, input().split())))

print(scores[-n])
