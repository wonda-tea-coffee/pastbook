import bisect

N, K = map(int, input().split())
A = list(map(int, input().split()))

b = bisect.bisect_left(A, K)
if b == N:
    print(-1)
else:
    print(b)
