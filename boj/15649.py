import sys

N, M = map(int, sys.stdin.readline().split())
select = []
boollist = [False for _ in range(0,N)]

def DFS(count):
    if count == M:
        for i in select:
            print(i, end = ' ')
        print('')
        return

    for i in range(1, N+1):
        if boollist[i-1]:
            continue
        boollist[i-1] = True
        select.append(i)
        DFS(count + 1)
        boollist[i-1] = False
        select.pop()

DFS(0)

'''
boj
N and M (1) (15649)
29028KB / 284ms
'''