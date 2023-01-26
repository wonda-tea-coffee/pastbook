def has_bit(n, i):
    return (n & (1<<i)) > 0

N = int(input())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))
ALL = 1<<N
cost = [[10**100] * N for _ in range(ALL)]
# print(A)
cost[0][0] = 0
for n in range(ALL):
    for i in range(N):
        for j in range(N):
            if has_bit(n, j) or i == j:
                continue

            # print(cost[n|j])
            cost[n|1<<j][j] = min(cost[n|1<<j][j], cost[n][i] + A[i][j])

print(cost[ALL-1][0])
