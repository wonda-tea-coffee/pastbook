from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
F = [False] * (N+1)
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

queue = deque()
F[1] = True
queue.append((1, 0))
while len(queue) > 0:
    s, c = queue.popleft()

    for ns in G[s]:
        if not F[ns] and c < 2:
            F[ns] = True
            queue.append((ns, c+1))

if F[N]:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
