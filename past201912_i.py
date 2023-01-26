N, M = map(int, input().split())
S = [0]
C = [0]
for i in range(M):
    si, ci = input().split()

    s_val = 0
    for j in range(N):
        if si[j] == 'Y':
            s_val |= 1 << j

    S.append(s_val)
    C.append(int(ci))

INF = 10**100
ALL = 1 << N
dp = [[INF] * ALL for _ in range(M+1)]
dp[0][0] = 0
for i in range(1, M+1):
    for j in range(ALL):
        dp[i][j] = min(dp[i][j], dp[i-1][j])
        k = j | S[i]
        dp[i][k] = min(dp[i][k], dp[i-1][j] + C[i])

if dp[M-1][ALL-1] == INF:
    print(-1)
else:
    print(dp[M-1][ALL-1])
