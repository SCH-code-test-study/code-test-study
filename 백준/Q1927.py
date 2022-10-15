# min 함수로 구현, 시간 초과
import sys

input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(min(arr))
            arr.remove(min(arr))
    else:
        arr.append(x)

# heap 라이브러리 사용
import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n) :
    x = int(input())
    if x == 0 :
        if heap:
            print(heapq.heappop(heap))
        else :
            print(0)
    else :
        heapq.heappush(heap, x)

'''
단순한 순차 탐색으로 최댓값, 최솟값을 찾을 경우 O(N)의 탐색 시간이 소요된다.

하지만, 힙의 경우 O(logN), 즉 트리의 높이만큼만 비교를 하게된다.

https://velog.io/@jaenny/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%ED%9E%99-%EC%B5%9C%EC%86%8C%ED%9E%99-%EC%B5%9C%EB%8C%80%ED%9E%99#heap--0-1-3-2-4-7-6-5-%EC%97%90%EC%84%9C-%EC%B5%9C%EC%86%8C%EA%B0%92-%EC%82%AD%EC%A0%9C%ED%95%98%EA%B8%B0
'''