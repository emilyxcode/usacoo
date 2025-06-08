import sys
from collections import defaultdict
sys.stdin = open("3.in")

N, F = [int(e) for e in input().strip().split()]
con = input().strip()


def isMoo(tri):
    if tri[1] == tri[2]:
        return True
    return False

mem = defaultdict(int)

for i in range(N-2):
    tri = con[i:i + 3]
    if isMoo(tri):
        mem[tri] += 1

ans = set()
for k, v in mem.items():
    if v >= F - 1:
        ans.add(k)

for i in range(N):
    
b = 0