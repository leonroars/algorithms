"""
BOJ #10818

Q. N number of integers are given. Return minimum and maximum of input.

Input
- On the first line, total number of input(input size) is given.
- On the second line, input is given(sequence of integers)
- -1_000_000<=Input Integers<= +1_000_000

Output
- Return minimum and maximum of input. They must be returned as space-sperated.

Condition
- Time: 1s
- Space: 256MB
"""
import sys
inpt_size = int(input())
inpt = list(map(int, sys.stdin.readline().split(" ")))

# There can be exception if min and max is initialized with '0' 
# - There can be a sequence of integers which has a integer that greater than 0 as its minimum. In this case, there'd be no chance for min to be updated.
 
min = inpt[0]
max = inpt[0]


for _ in inpt:
    if _ < min:
        min = _
    elif _ > max:
        max = _
    else:
        continue

print("{} {}".format(min, max))