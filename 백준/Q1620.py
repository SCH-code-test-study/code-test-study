# 시간 초과
# 리스트에서 탐색을 할 경우 시간복잡도는 O(n)
n, m = map(int, input().split())
stack = []

for _ in range(n):
    stack.append(input())

for _ in range(m):
    inputPoketmon = input()
    if inputPoketmon.isdigit():
        print(stack[int(inputPoketmon)-1])
    else:
        print(stack.index(inputPoketmon)+1)

# 딕셔너리 자료구조 사용
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}

for i in range(1, n+1):
    inputPoketmon = input().rstrip()
    dict[i] = inputPoketmon
    dict[inputPoketmon] = i

for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(dict[int(quest)])
    else:
        print(dict[quest])