N = int(input())
M = 101
c = [[] for _ in range(M)]
for i in range(N):
    Ai, Bi = map(int, input().split())
    c[Bi].append(Ai)

for i in range(M):
    c[i].sort()

ans = 0
# print(c)
for i in range(1, N+1):
    for j in range(M-1, 0, -1):
        if len(c[j]) == 0:
            continue

        if c[j][0] <= i:
            ans += j
            print(ans)
            c[j].remove(c[j][0])
            break
