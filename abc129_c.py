N, M = map(int, input().split())
a = set()
for i in range(M):
    a.add(int(input()))
dp = [0] * (N+1)
MOD = 1000000007

dp[0] = 1
if not 1 in a:
    dp[1] = 1
for i in range(2, N+1):
    if i in a:
        continue

    dp[i] = (dp[i-1] + dp[i-2]) % MOD

print(dp[N])
