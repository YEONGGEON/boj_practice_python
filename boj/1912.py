import sys

N = int(sys.stdin.readline())
llist = list(map(int, sys.stdin.readline().split()))

temp = llist[0]
largest = llist[0]

for i in range(1,N):
    if temp > 0 and temp + llist[i] >= 0:
        temp += llist[i]
    else:
        temp = llist[i]

    if largest < temp:
        largest = temp

print(largest)