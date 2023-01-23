def out():
    for i in range(N):
        print("".join(G[i]))

N, Q = map(int, input().split())
G = [["N"] * (N) for i in range(N)]

# print(G)

for i in range(Q):
    S = list(map(int, input().split()))
    # print("S:", S)
    a = S[1] - 1
    if S[0] == 1:
        b = S[2] - 1
        G[a][b] = "Y"
    elif S[0] == 2:
        for j in range(N):
            if G[j][a] == "Y":
                G[a][j] = "Y"
    elif S[0] == 3:
        X = []
        for x in range(N):
            if G[a][x] == "Y":
                for y in range(N):
                    if y != a and G[x][y] == "Y":
                        X.append(y)
        for x in X:
            G[a][x] = "Y"

out()
