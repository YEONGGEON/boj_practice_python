import sys

frontnum = 0

def push(A, B):
    A.append(B)

def pop(A):
    global frontnum
    if len(A)==0 or len(A) == frontnum:
        return -1
    else:
        popnum = A[frontnum]
        frontnum += 1
        return popnum

def front(A):
    global frontnum
    if len(A)==0 or len(A) == frontnum:
        return -1
    else:
        return A[frontnum]

def back(A):
    if len(A)==0 or len(A) == frontnum:
        return -1
    else:
        return A[-1]

def size(A):
    return len(A) - frontnum

def empty(A):
    if len(A)==0 or len(A) == frontnum:
        return 1
    else:
        return 0

stack_list = []
times = int(sys.stdin.readline())
for i in range(0,times):
    input_str = str(sys.stdin.readline())
    if  "push" in input_str:
        A, B=input_str.split()
        push(stack_list, int(B))
    elif input_str == 'pop\n':
        print(pop(stack_list))
    elif input_str == 'size\n':
        print(size(stack_list))
    elif input_str == 'empty\n':
        print(empty(stack_list))
    elif input_str == 'front\n':
        print(front(stack_list))
    elif input_str == 'back\n':
        print(back(stack_list))