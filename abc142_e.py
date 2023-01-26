N, M = map(int, input().split())
a = [0]
c = [0]
for i in range(M):
    ai, bi = map(int, input().split())
    s = list(map(int, input().split()))
    c_val = 0
    for si in s:
        c_val |= 1<<(si-1)

    a.append(ai)
    c.append(c_val)

INF = 10**100
ALL = 1<<N
dp = [[INF] * ALL for _ in range(M+1)]
dp[0][0] = 0
# print(dp)
# print("c:", c)
for i in range(1, M+1):
    for n in range(ALL):
        dp[i][n]      = min(dp[i][n],      dp[i-1][n])
        dp[i][n|c[i]] = min(dp[i][n|c[i]], dp[i-1][n] + a[i])

if dp[M][ALL-1] == INF:
    print(-1)
else:
    print(dp[M-1][ALL-1])
