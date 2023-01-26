N, M, X = map(int, input().split())
C = []
A = []
for i in range(N):
    s = list(map(int, input().split()))
    C.append(s[0])
    A.append(s[1:])

INF = 10**100
ans = INF
# 買い方の組み合わせ
for i in range(2**N):
    comprehension = [0] * M
    cost = 0
    for j in range(N):
        if i >> j & 1:
            cost += C[j]
            for k in range(M):
                comprehension[k] += A[j][k]

    f = True
    for c in comprehension:
        f &= c >= X

    if f:
        ans = min(ans, cost)

if ans == INF:
    print(-1)
else:
    print(ans)
