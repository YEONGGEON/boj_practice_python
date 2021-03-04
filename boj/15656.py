import sys

N, M = map(int, sys.stdin.readline().split())
llist = list(map(int, sys.stdin.readline().split()))
llist.sort()
select = []

def DFS(count):
    if count == M:
        for i in select:
            print(i, end=' ')
        print('')
        return

    for i in range(0,N):
        select.append(llist[i])
        DFS(count + 1)
        select.pop()

DFS(0)

'''
boj
N and M (7) (15656)
28776KB / 3096ms
'''