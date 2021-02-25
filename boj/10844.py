import sys

llnum = int(1e9)
def stair(a):
    temp = [0,0,0,0,0,0,0,0,0,0]
    temp[1] += a[0]%llnum
    for i in range(1,9):
        temp[i-1] += a[i]%llnum
        temp[i+1] += a[i]%llnum
    temp[8] += a[9]%llnum
    return temp
        
N = int(sys.stdin.readline())
a = [0,1,1,1,1,1,1,1,1,1]

for _ in range(0,N-1):
    a = stair(a)

ans = 0
for i in a:
    ans += i
print(ans%llnum)

'''
boj
Easy Stair Number (10844)
28776KB / 64ms
'''