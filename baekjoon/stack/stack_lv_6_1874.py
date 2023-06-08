import sys

given_seq = []
seq_size = int(sys.stdin.readline())

for i in range(seq_size):
    each_num = int(sys.stdin.readline())
    given_seq.append(each_num)

turn_point = given_seq.index(seq_size)
post_turnpoint = given_seq[turn_point+1:]
for_check = sorted(post_turnpoint, reverse=True)

if post_turnpoint != for_check:
    print("NO")

else:
    operations_stack = []
    sorted_given_seq = [num for num in range(1, seq_size+1)]
    for j in given_seq:
        indicator = 1
        