import sys

N = int(sys.stdin.readline())
llist = []

for _ in range(N):
    llist.append(int(sys.stdin.readline()))

if N == 1:
    print(llist[0])
elif N == 2:
    print(llist[0] + llist[1])
else:
    score = [llist[0], llist[0] + llist[1], max(llist[0] + llist[2], llist[1]+llist[2])]

    for i in range(3,N):
        score.append(max(llist[i] + llist[i-1]+ score[i-3], llist[i] + score[i-2]))

    print(score[-1])

'''
boj
Climbing Stair (2579)
28776KB / 68ms
'''