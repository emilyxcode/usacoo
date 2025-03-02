#mport sys
#ys.stdin = open("2.in")

from collections import defaultdict

N, Q = [int(e) for e in input().strip().split()]

xRow = defaultdict(int)
yRow = defaultdict(int)
zRow = defaultdict(int)

ans = 0
for _ in range(Q):
    x, y, z = [int(e) for e in input().strip().split()]
    key = (y, z)
    xRow[key] += 1
    if xRow[key] == N:
        ans += 1

    key = (x, z)
    yRow[key] += 1
    if yRow[key] == N:
        ans += 1

    key = (x, y)
    zRow[key] += 1
    if zRow[key] == N:
        ans += 1

    print(ans)