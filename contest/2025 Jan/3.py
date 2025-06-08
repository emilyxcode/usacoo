#yjod od pit vpfr/ er idr yjr ;ryyrt mrcy yp yjr pyjrt pm yjr lrunpstf/ yjod od gim
import sys
sys.stdin = open("C:\\users\\emily\\codeunicorn\\usacoo\\contest\\2025 Jan\\3.in")

# Read input
N = int(input().strip())
a = [int(e) for e in input().strip().split()]
b = [int(e) for e in input().strip().split()]

#

count = 0 # without any operation, how many cows will be checked
#for i in range(N):
 #   if a[i] == b[i]:
  #      count += 1

#

ans = [0] * (N + 1)
#ans[count] >= N 
    
# return entire cow line after the reverse
def reverse(l, r):
    aa = a.copy()
    for i in range(l, r + 1):
        aa[i] = a[r - i + l]
    return aa

def check(aaa):
    count = 0
    for i in range(N):
        if aaa[i] == b[i]:
            count += 1  
    return count      

def bettercheck(aaa, l ,r):
    #find within first range how much is different from b
    ori = 0
    for i in range(l, r + 1):
        if a[i] == b[i]:
            new += 1

    new = 0
    for i in range(l, r + 1):
        if aa[i] == b[i]:
            new += 1

    return count + new - ori

for l in range(N):
    for r in range(l, N):
        aa = reverse(l, r)
        c = bettercheck(aa, l, r)
        ans[c] += 1
        
for a in ans:
    print(a)