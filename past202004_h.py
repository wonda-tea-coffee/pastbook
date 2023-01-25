import sys

INF = 10**100
N, M = map(int, input().split())
A = []
for i in range(N):
    A.append(input())
cost = [[INF] * M for _ in range(N)]

h = {}
for i in range(N):
    for j in range(M):
        if A[i][j] in h:
            h[A[i][j]].append((i, j))
        else:
            h[A[i][j]] = [(i, j)]

cost[h['S'][0][0]][h['S'][0][1]] = 0
C = ['S', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'G']
for i in range(len(C) - 1):
    if not C[i] in h or not C[i+1] in h:
        continue
    for sy, sx in h[C[i]]:
        for gy, gx in h[C[i+1]]:
            cost[gy][gx] = min(cost[gy][gx], abs(gy - sy) + abs(gx - sx) + cost[sy][sx])

# print(h)
# print(cost)
gy, gx = h['G'][0]
if cost[gy][gx] == INF:
    print(-1)
else:
    print(cost[gy][gx])
