N = int(input())
p = list(map(int, input().split()))
M = sum(p)

dp = [[False] * (M+1) for _ in range(N)]
dp[0][0] = True
dp[0][p[0]] = True
for i in range(1, N):
    dp[i][0] = True
    for j in range(M+1):
        dp[i][j] = dp[i-1][j]
        if j - p[i] >= 0 and dp[i-1][j-p[i]]:
            dp[i][j] = True

ans = 0
for i in range(M+1):
    if dp[N-1][i]:
        ans += 1

print(ans)
