"""
BOJ #10807
Q. For given N number of integer, write a program that counts the number of interger 'v'.

Input
- On the first line, total number of integer - the number of input - is given.
- On the second line, specified number of integers sperated by space is given as input.
- On the third line, target integer is given.

Output
- Return counted target integer in input.
"""
import sys

inpt_size = int(input())
inpt = list(map(int, sys.stdin.readline().split(" ")))
target = int(input())
cnt = 0
for _ in inpt:
    if _ == target:
        cnt+=1
print(cnt)