import sys

N, M = map(int, sys.stdin.readline().split())
llist = list(map(int, sys.stdin.readline().split()))
llist.sort()
strllist = []
for i in llist:
    strllist.append(str(i))
select = []
setselect = set()
boollist = [0] * N

def DFS(a,count):
    if count == M:
        inputstr = ' '.join(select)
        if inputstr not in setselect:
            print(inputstr)
            setselect.add(inputstr)
        return

    for i in range(a,N):
        if  boollist[i] == 1:
            continue
        select.append(strllist[i])
        boollist[i] = 1
        DFS(i,count + 1)
        select.pop()
        boollist[i] = 0

DFS(0,0)

'''
boj
N and M (10) (15664)
28776KB / 68ms
'''