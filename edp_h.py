H, W = map(int, input().split())
G = [None] * H
dist = [[0] * W for i in range(H)]
MOD = 10**9 + 7
for i in range(H):
    G[i] = input()

for hi in range(H):
    if G[hi][0] == "#":
        break
    dist[hi][0] = 1

for wi in range(W):
    if G[0][wi] == "#":
        break
    dist[0][wi] = 1

for hi in range(1, H):
    for wi in range(1, W):
        if G[hi][wi] == "#":
            continue

        dist[hi][wi] = (dist[hi-1][wi] + dist[hi][wi-1]) % MOD

print(dist[H-1][W-1])
