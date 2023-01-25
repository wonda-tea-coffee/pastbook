def rec(n):
    if done[n]:
        return length[n]

    length[n] = 0
    for m in edges[n]:
        length[n] = max(length[n], rec(m) + 1)

    done[n] = True
    return length[n]

import sys
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())
edges = []
for i in range(N):
    edges.append([])
indeg = [0] * N
length = [0] * N
done = [False] * N

for i in range(M):
    x, y = map(int, input().split())
    edges[x-1].append(y-1)
    indeg[y-1] += 1

for i in range(N):
    if indeg[i] == 0:
        rec(i)

print(max(length))
