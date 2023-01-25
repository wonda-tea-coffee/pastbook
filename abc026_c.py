import sys
sys.setrecursionlimit(1000000)

def solve(n):
    s = []
    for i in range(2, N+1):
        if B[i] == n:
            s.append(solve(i))

    if len(s) == 0:
        return 1
    elif len(s) == 1:
        return 2*s[0]+1
    else:
        return max(s) + min(s) + 1

N = int(input())
B = [0, 0]
for i in range(N-1):
    B.append(int(input()))

print(solve(1))
