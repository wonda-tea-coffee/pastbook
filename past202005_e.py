N, M, Q = map(int, input().split())
L = [[] for i in range(N + 1)]
for i in range(M):
    u, v = map(int, input().split())
    L[u].append(v)
    L[v].append(u)
C = [None] + list(map(int, input().split()))
O = []

for i in range(Q):
    si = list(map(int, input().split()))
    x = si[1]
    O.append(C[x])
    if si[0] == 1:
        for j in L[x]:
            C[j] = C[x]
    elif si[0] == 2:
        C[x] = si[2]

for oi in O:
    print(oi)
