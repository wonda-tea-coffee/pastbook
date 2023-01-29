# 最小全域木
# プリム法

import heapq

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    u, v, c = map(int, input().split())
    G[u].append((v, c))
    G[v].append((u, c))

marked = [False] * N
marked[0] = True
marked_count = 1
Q = []

for v, c in G[0]:
    heapq.heappush(Q, (c, v))

ans = 0
while marked_count < N:
    c, i = heapq.heappop(Q)

    if marked[i]:
        continue

    marked[i] = True
    marked_count += 1
    ans += c

    for j, c in G[i]:
        if marked[j]:
            continue

        heapq.heappush(Q, (c, j))

print(ans)
