N, K = map(int, input().split())
A = list(map(int, input().split()))

l = 0
r = N-1
while l < r:
    m = (l+r)//2
    # print(l, m, r)
    if A[m] >= K:
        r = m
    else:
        l = m+1
# print(l, m, r)
if A[l] >= K:
    print(l)
else:
    print(-1)
