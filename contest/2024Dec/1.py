import sys
sys.stdin = open("C:\\Users\\emily\\codeunicorn\\temp\\2024Dec\\1.in")

def round(n, d): # n is the number to be rounded. d is the number rounded to (such as 10, 100, 1000, 10000...)
    if n % d < d // 2:
         return n - n % d
    else:
         return n + d - n % d

def chain_round(n, d):
    ten = 10
    while ten <= d:
         n = round(n, ten)
         ten *= 10
    return n

def solve(strN):
    N = int(strN)
    digitNum = len(strN)
    ret = 0
    for i in range(2, digitNum + 1):
         upper = int('5' + '0' * (i - 1))
         upper = min(upper, N + 1)
         lower = int('4' * (i - 1) + '5')
         if upper > lower:
            ret += (upper - lower)
         else: 
            continue
    
    return ret


T = int(input().strip())
for i in range(T):
    strN = input().strip()

    print(solve(strN))