import sys

N, M = map(int, sys.stdin.readline().split())
llist = list(map(int, sys.stdin.readline().split()))
llist.sort()
select = []

def DFS(a, count):
    if count == M:
        for i in select:
            print(i, end=' ')
        print('')
        return

    for i in range(a,N):
        select.append(llist[i])
        DFS(i,count + 1)
        select.pop()

DFS(0,0)

'''
boj
N and M (8) (15657)
28776KB / 92ms
'''