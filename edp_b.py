N, K = map(int, input().split())
h = list(map(int, input().split()))
dp = [0] * N

for i in range(1, N):
    m = 10 ** 18
    ki = 1
    while ki <= K and i - ki >= 0:
        m = min(m, abs(h[i] - h[i - ki]) + dp[i - ki])
        ki += 1
    dp[i] = m

# print(dp)
print(dp[N - 1])
