import sys

numberOfCommand = int(sys.stdin.readline())
q = []
front = 0
back = -1
for i in range(numberOfCommand):
    com = sys.stdin.readline().rstrip()
    com_lst = com.split(" ")
    if com_lst[0] == "push":
        q.append(int(com_lst[1]))
        back += 1
    elif com_lst[0] == "pop":
        if back == -1:
            print(back)
        else:
            pop_num = q.pop(front)
            print(pop_num)
            back -= 1
    elif com_lst[0] == "size":
        print(len(q))
    elif com_lst[0] == "empty":
        if not q:
            print(0)
        if q:
            print(1)
    elif com_lst[0] == "front":
        if back == -1:
            print(back)
        else:
            print(q[front])
    elif com_lst[0] == "back":
        if back == -1:
            print(back)
        else:
            print(q[back])
    else:
        print("error")
        break