N, W = map(int, input().split())
w = [None] * N
v = [None] * N
for i in range(N):
    w[i], v[i] = map(int, input().split())

INF = 10 ** 18
MAX = 10**3 * 100
dp = [[INF] * (MAX+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(1, N+1):
    for j in range(MAX+1):
        if j - v[i-1] >= 0:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-v[i-1]] + w[i-1])
        else:
            dp[i][j] = dp[i-1][j]

for j in range(MAX, 0, -1):
    # print(N, j)
    if dp[N][j] <= W:
        print(j)
        break
