import sys
sys.setrecursionlimit(1000000)

def dfs(y, x):
    visited[y][x] = True

    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny = y + d[0]
        nx = x + d[1]
        if ny >= 0 and ny < H and nx >= 0 and nx < W and not visited[ny][nx] and not G[ny][nx] == "#":
            dfs(ny, nx)

H, W = map(int, input().split())
G = []
for i in range(H):
    G.append(input())

visited = [[False] * W for i in range(H)]

for i in range(H):
    for j in range(W):
        if G[i][j] == "s":
            si, sj = i, j
        elif G[i][j] == "g":
            gi, gj = i, j

dfs(si, sj)

if visited[gi][gj]:
    print("Yes")
else:
    print("No")
