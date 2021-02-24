import sys
import math

rooms = int(sys.stdin.readline())
people = list(map(int, sys.stdin.readline().split()))
mainman, subman = map(int, sys.stdin.readline().split())

totmen = 0
for i in people:
    if mainman > i:
        totmen += 1
    else:
        totmen += math.ceil(((i-mainman)/subman)) + 1

print(totmen)
