import sys
import heapq

upper= []
lower = []
middle = 0
start = True
for i in range(int(sys.stdin.readline())):
    inputnum = int(sys.stdin.readline())

    if start:
        middle = inputnum
        start = False
        print(inputnum)
        continue

    if middle < inputnum:
        heapq.heappush(upper, inputnum)
    else:
        heapq.heappush(lower, -1 * inputnum)

    if len(upper) - len(lower) > 1:
        heapq.heappush(lower, middle * -1)
        middle = heapq.heappop(upper)
    if len(lower) - len(upper) > 1:
        heapq.heappush(upper, middle)
        middle = heapq.heappop(lower) * -1

    if len(lower) == len(upper):
        print(middle)
    if len(lower) - len(upper) == 1:
        print(min(lower[0] * -1, middle))
    if len(upper) - len(lower) == 1:
        print(min(upper[0], middle))