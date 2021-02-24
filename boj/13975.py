import sys
import heapq

for _ in range(int(sys.stdin.readline())):
    heap = []
    times = int(sys.stdin.readline())
    innum = list(map(int, sys.stdin.readline().split()))
    for i in range(times):
        heapq.heappush(heap,innum[i])
    
    price = 0
    while len(heap) > 1:
        temp = heapq.heappop(heap) + heapq.heappop(heap)
        price += temp
        heapq.heappush(heap, temp)

    print(price)