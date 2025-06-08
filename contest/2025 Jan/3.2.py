#import sys
#sys.stdin = open("C:\\users\\emily\\codeunicorn\\usacoo\\contest\\2025 Jan\\3.in")

# Read input
N = int(input().strip())
a = [int(e) for e in input().strip().split()]
b = [int(e) for e in input().strip().split()]


count = 0 # without any operation, how many cows will be checked
for i in range(N):
    if a[i] == b[i]:
        count += 1

#

ans = [0] * (N + 1)
#ans[count] >= N 


for c in range(N):
    newCount = count
    for i in range(N):
        #[c - i, c + i]
        if c - i < 0 or c + i >= N:
            break
        if a[c - i] == b[c - i]:
            newCount -= 1
        if a[c + i] == b[c + i]:
            newCount -= 1
        if a[c - i] == b[c + i]:
            newCount += 1
        if a[c + i] == b[c - i]:
            newcount += 1
        ans[newCount] += 1

    #if no centre
    newCount = count
    for i in range(N):
        if c - i < 0 or c + i + 1 >= N:
            break
        if a[c - i] == b[c - i]:
            newCount -= 1
        if a[c+ 1 + i] == b[c + 1 + i]:
            newCount -=1
        if a[c - i] == b[c + i + 1]:
            newCount += 1
        if a[c + i + 1] == b[c - i]:
            newCount += 1
        ans[newCount] += 1

        
for a in ans:
    print(a)