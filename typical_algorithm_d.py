import heapq

N, M = map(int, input().split())
G = [[] for _ in range(N)]
dist = [-1] * N
for i in range(M):
    u, v, c = map(int, input().split())
    G[u].append((v, c))

Q = []
heapq.heappush(Q, (0, 0))
dist[0] = 0
done = [False] * N

while len(Q) > 0:
    d, v = heapq.heappop(Q)

    if v == N-1:
        print(d)
        break

    if done[v]:
        continue

    done[v] = True

    for nv, c in G[v]:
        if dist[nv] == -1 or dist[nv] > d+c:
            dist[nv] = d+c
            heapq.heappush(Q, (d+c, nv))
