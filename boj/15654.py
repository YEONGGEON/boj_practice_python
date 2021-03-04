import sys

N, M = map(int, sys.stdin.readline().split())
llist = list(map(int, sys.stdin.readline().split()))
llist.sort()
boollist = [0] * N
select = []

def DFS(count):
    if count == M:
        for i in select:
            print(i, end=' ')
        print('')
        return

    for i in range(0,N):
        if boollist[i] == 1:
            continue
        select.append(llist[i])
        boollist[i] = 1
        DFS(count + 1)
        select.pop()
        boollist[i] = 0

DFS(0)

'''
boj
N and M (5) (15654)
28776KB / 288ms
'''