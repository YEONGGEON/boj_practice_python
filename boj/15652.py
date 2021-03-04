import sys

N, M = map(int, sys.stdin.readline().split())
select = [0]

def DFS(count):
    if count == M:
        for i in range(1,M+1):
            print(select[i], end = ' ')
        print('')
        return

    for i in range(1, N+1):
        if i >= select[-1]:
            select.append(i)
            DFS(count + 1)
            select.pop()

DFS(0)

'''
boj
N and M (4) (15652)
29028KB / 96ms
'''