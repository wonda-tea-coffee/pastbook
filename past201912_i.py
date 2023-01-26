N, M = map(int, input().split())
S = [0]
C = [0]
for i in range(M):
    s, c = input().split()
    s_val = 0
    for j in range(N):
        if s[j] == 'Y':
            s_val |= 1<<j
    S.append(s_val)
    C.append(int(c))

ALL = 1<<N
INF = 10**100
cost = [[INF] * ALL for _ in range(M+1)]

cost[0][0] = 0
for i in range(1, M+1):
    for n in range(ALL):
        cost[i][n] = min(cost[i][n], cost[i-1][n])
        cost[i][n|S[i]] = min(cost[i][n|S[i]], cost[i-1][n] + C[i])

if cost[M][ALL-1] == INF:
    print(-1)
else:
    print(cost[M][ALL-1])
