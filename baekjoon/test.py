import sys

nums = map(int, sys.stdin.readlines().split())
ans = 0
for i in nums:
    ans += i
print(ans)