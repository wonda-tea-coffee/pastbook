N, W = map(int, input().split())
w = []
v = []
for i in range(N):
    wi, vi = map(int, input().split())
    w.append(wi)
    v.append(vi)

dp = [[0] * (W + 1) for i in range(N)]
dp[0][w[0]] = v[0]

for i in range(1, N):
    for j in range(W + 1):
        dp[i][j] = dp[i - 1][j]
        if j >= w[i]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - w[i]] + v[i])

ans = 0
for i in range(W + 1):
    ans = max(ans, dp[N - 1][i])

print(ans)
