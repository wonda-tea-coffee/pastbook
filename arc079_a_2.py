import heapq

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
F = [False] * (N+1)
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

Q = []
F[1] = True
heapq.heappush(Q, (0, 1))
while len(Q) > 0:
    d, v = heapq.heappop(Q)

    for nv in G[v]:
        if not F[nv] and d < 2:
            F[nv] = True
            heapq.heappush(Q, (d+1, nv))

if F[N]:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
