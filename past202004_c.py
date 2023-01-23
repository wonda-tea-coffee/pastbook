N = int(input())
M = 2 * N - 1
G = []
for i in range(N):
    G.append(list(input()))

for i in range(N - 2, -1, -1):
    for j in range(1, 2 * N - 1):
        if G[i][j] == "#":
            if G[i + 1][j - 1] == "X" or G[i + 1][j] == "X" or G[i + 1][j + 1] == "X":
                G[i][j] = "X"

for i in range(N):
    print(''.join(G[i]))
