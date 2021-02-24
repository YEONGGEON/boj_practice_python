from sys import stdin

A = int(stdin.readline())
B = int(stdin.readline())

def minnum(A, B):
    time = 0
    for i in range(1,B+1):
        if B < A//i:
            time += B
        else:
            time += A//i
    return time

left = 1
right = B**2

while left <= right:
    middle = (left+right)//2
    
    if minnum(middle, A) < B:
        left = middle + 1
    elif minnum(middle, A) >= B:
        right = middle - 1

print(left)