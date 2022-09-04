# 출력 초과, 노가다로 푸는 격
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

notHear = {}
notSee = {}
common = []

for i in range(n):
    notHearPerson = input().rstrip()
    notHear[i] = notHearPerson

for i in range(m):
    notSeePerson = input().rstrip()
    notSee[notSeePerson] = i

for i in notHear.values():
    print(i)
    if notSee.get(i) != None:
        common.append(i)

common.sort()

print(common)

for i in common:
    print(i)

# set 자료형 활용
n, m = map(int, input().split())

a = set()
for i in range(n):
    a.add(input())

b = set()
for i in range(m):
    b.add(input())

result = sorted(list(a & b))

print(len(result))

for i in result:
    print(i)