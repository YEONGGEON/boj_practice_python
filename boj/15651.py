import sys

N, M = map(int, sys.stdin.readline().split())
select = []

def DFS(count):
    if count == M:
        for i in select:
            print(i, end = ' ')
        print('')
        return

    for i in range(1, N+1):
        select.append(i)
        DFS(count + 1)
        select.pop()

DFS(0)

'''
boj
N and M (3) (15651)
29028KB / 2948ms
'''