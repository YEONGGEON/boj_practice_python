import sys

time = int(sys.stdin.readline())
in_list = list(map(int, sys.stdin.readline().split()))
st_list = []
ans_list = []

for i in reversed(in_list):
    if len(st_list) == 0:
        ans_list.append(-1)
        st_list.append(i)
    elif i >= st_list[-1]:
        while True:
            st_list.pop()
            if len(st_list) == 0:
                ans_list.append(-1)
                st_list.append(i)
                break
            elif i < st_list[-1]:
                ans_list.append(st_list[-1])
                st_list.append(i)
                break
    else:
        ans_list.append(st_list[-1])
        st_list.append(i)

for j in reversed(ans_list):
    print(j, end=' ')