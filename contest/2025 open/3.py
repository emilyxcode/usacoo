import sys
sys.stdin = open('3.in')

# read input
N, Q = [int(e) for e in input().strip().split()]
s = input().strip()

first_m_lookup = []
last_o_lookup = []
first_o_lookup = []

for i in range(26):
    ch = chr(ord('a') + i)

    lu = [-1] * N
    cur = -1
    for j in range(N - 1, -1, -1):
        if s[j] != ch:
            cur = j
        lu[j] = cur
    first_m_lookup.append(lu)

    lu = [-1] * N
    cur = -1
    for j in range(N):
        if s[j] == ch:
            cur = j
        lu[j] = cur
    last_o_lookup.append(lu)

    lu = [-1] * N
    cur = -1
    for j in range(N - 1, -1, -1):
        if s[j] == ch:
            cur = j
        lu[j] = cur
    first_o_lookup.append(lu)

def solve(l, r):
    ans = -1
    # brute force 26 letters [moo]
    for i in range(26):
        ch = chr(ord('a') + i) # for moo with this ch as 'o'
        
        #find first m
        first_m = first_m_lookup[i][l]

        #find last o
        last_o = last_o_lookup[i][r]

        if first_m >= r:
            continue
        if last_o <=l:
            continue
        if first_m >= last_o - 1:
            continue
        # find middle
        middle = (first_m + last_o)//2
        if middle == ch:
            ans = max(ans, (last_o - middle) * (middle - first_m))
            continue 
        else:
            first_o = last_o_lookup[i][middle]
            if first_o <= first_m:
                pass
            else: 
                ans = max(ans, (last_o - first_o) * (first_o - first_m))

            first_o = first_o_lookup[i][middle]
            if first_o >= last_o:
                pass
            else:
                ans = max(ans, (last_o - first_o) * (first_o - first_m))

        # if middle = o, we are lucky

        # else, we are not lucky

        # find closest o to the middle
    return ans
        
        

for _ in range(Q):
    l, r = [int(e) -  1 for e in input().strip().split()]
    print(solve(l, r))