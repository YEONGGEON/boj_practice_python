import sys

N = int(sys.stdin.readline())
tri = []
anstri = []

for _ in range(0,N):
    tri.append(list(map(int, sys.stdin.readline().split())))
    anstri.append([])

anstri[0].append(tri[0][0])

for i in range(1,N):
    for j in range(0,i+1):
        if j == 0:
            anstri[i].append(anstri[i-1][0] + tri[i][0])
        elif j == i:
            anstri[i].append(anstri[i-1][-1] + tri[i][-1])
        else:
            anstri[i].append(max(anstri[i-1][j-1],anstri[i-1][j]) + tri[i][j])

print(max(anstri[-1]))

'''
boj
Integer Triangle (1932)
38432KB / 184ms
'''