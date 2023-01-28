N, K = map(int, input().split())
A = list(map(int, input().split()))

l = 0
r = N-1
ans = -1
while l < r:
    m = (l+r)//2
    if A[m] >= K:
        r = m
        ans = m
    else:
        l = m+1

print(ans)
